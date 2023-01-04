import bitio
import huffman
import pickle
Debug = False


def read_tree(tree_stream):
    '''Read a description of a Huffman tree from the given compressed
    tree stream, and use the pickle module to construct the tree object.
    Then, return the root node of the tree itself.
    Args:
      tree_stream: The compressed stream to read the tree from.
    Returns:
      A Huffman tree root constructed according to the given description.
    '''
    loadedtree = pickle.load(tree_stream)
    return loadedtree


def decode_byte(tree, bitreader):
    """
    Reads bits from the bit reader and traverses the tree from
    the root to a leaf. Once a leaf is reached, bits are no longer read
    and the value of that leaf is returned.
    Args:
      bitreader: An instance of bitio.BitReader to read the tree from.
      tree: A Huffman tree.
    Returns:
      Next byte of the compressed bit stream.
    """
    TreeEnd = False
    while not TreeEnd:
        stringbit = str(bitreader.readbit())
        # if Debug: print("-----------"+"stringbitL38", stringbit)
        if '0' == stringbit:
            # its zero, go left
            tree = tree.getLeft()
            # if isinstance(tree, huffman.TreeLeaf):
            #     # if the node reached is a leaf
            #     return tree.getValue()
            #     if Debug: print(" line 44 nodevalue", Value)
            #     # get value of the leaf
            #     # create a brand new tree
            # else: # a node is reached
            #     decode_byte(tree, bitreader) # ->
            #     # recreate the tree starting from this
        elif '1' == stringbit:
            tree = tree.getRight()
        if isinstance(tree, huffman.TreeLeaf):
            TreeEnd = True
            return tree.getValue()
    # if isinstance(tree, huffman.TreeLeaf):
    # return tree.getValue()
    # #else:
    # #decode_byte(tree, bitreader)
    # #if Debug: print("-----------"+"valueL56", Value)


def decompress(compressed, uncompressed):
    '''First, read a Huffman tree from the 'compressed' stream using your
    read_tree function. Then use that tree to decode the rest of the
    stream and write the resulting symbols to the 'uncompressed'
    stream.
    Args:
      compressed: A file stream from which compressed input is read.
      uncompressed: A writable file stream to which the uncompressed
          output is written.
    '''
    # print('L78')
    tree = read_tree(compressed)
    # print(tree)
    bitreadstream = bitio.BitReader(compressed)
    bitwritestream = bitio.BitWriter(uncompressed)
    # end_of_file = False
    try:
        byteValue = decode_byte(tree, bitreadstream)
    except EOFError:
        byteValue = None
        # no more bits
    while byteValue is not None:
        try:
            bitwritestream.writebits(byteValue, 8)
            byteValue = decode_byte(tree, bitreadstream)
        # while not at EOF, keep calling the
        # decode_byte function with a new tree
        # print('hi')
        except EOFError:
            # print("line83 when byteValue is None")
            byteValue = True
    if Debug:
        print('flushed L94')
    # if you have a byte that is not 8
    # at the end, rests are 0
    pass


def write_tree(tree, tree_stream):
    '''Write the specified Huffman tree to the given tree_stream
    using pickle.
    Args:
      tree: A Huffman tree.
      tree_stream: The binary file to write the tree to.
    '''
    pickle.dump(tree, tree_stream)
    pass


def compress(tree, uncompressed, compressed):
    '''First write the given tree to the stream 'compressed' using the
    write_tree function. Then use the same tree to encode the data
    from the input stream 'uncompressed' and write it to 'compressed'.
    If there are any partially-written bytes remaining at the end,
    write 0 bits to form a complete byte.
    Flush the bitwriter after writing the entire compressed file.
    Args:
      tree: A Huffman tree.
      uncompressed: A file stream from which you can read the input.
      compressed: A file stream that will receive the tree description
          and the coded input data.
    '''
    write_tree(tree, compressed)
    # writing tree to the compressed
    # stream
    bitreadstream = bitio.BitReader(uncompressed)
    bitwritestream = bitio.BitWriter(compressed)
    encoding_Table = huffman.make_encoding_table(tree)
    end_of_file = False
    while not end_of_file:
        try:
            byte = bitreadstream.readbits(8)
            encodedByte = encoding_Table[byte]
            for bit in encodedByte:
                bitwritestream.writebit(bit)
        except EOFError:
            end_of_file = True
            EOFindicator = encoding_Table[None]
            for bit in EOFindicator:
                bitwritestream.writebit(bit)
    bitwritestream.flush()
