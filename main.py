import algo

# read file and return string
def read_file(file_name):
    with open(file_name, 'r') as f:
        return f.read()


# save to file with compression
def save_file(file_name, string):
    with open(file_name, 'w') as f:
        f.write(string)

# get arguments
def get_args():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help='string file')
    parser.add_argument('-o', '--output', help='output json keys name')
    parser.add_argument('-k', '--key', help='json key letter map')

    parser.add_argument('-e', '--encrypt', help='encrypto file', action='store_true')
    parser.add_argument('-d', '--decrypt', help='decrypto file', action='store_true')
    return parser.parse_args()


# main
if __name__ == '__main__':
    # if encrypt arg is persent
    if get_args().encrypt:
        encrypt = get_args().input
        key = get_args().key
        output = get_args().output
        # encrypto
        string = algo.encrypt_new(encrypt,key,output)
        # save to file
        print('Encrypted and saved at: ', output)
    if get_args().decrypt:
        # read file

        # decrypto
        decrypt = get_args().input
        key = get_args().key
        output = get_args().output
        string = algo.decrypt_new(decrypt,key,output)
        print('Decrypted at: ', output)
    else:
        # help screen
        # print all args
        print("You need atleast --input --output --ket and --decrypt or --encrypt")
