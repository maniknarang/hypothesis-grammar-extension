from hypothesis.strategies import composite, builds


@composite
def cfg(draw, cfg_file_path: str):
    # open file
    # parse file and get grammar in python classes
    # graph exploration to label min distances to terminals
    # generate random string from grammar w/ max depths
    result = "1+1"
    print(f"returning: {result}")
    return result
