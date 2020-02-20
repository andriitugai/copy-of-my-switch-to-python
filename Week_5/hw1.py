import argparse
import os
import zipfile


class dir_zipper:
    def __init__(self, path_to_zip_file, password):
        self.path_to_zip_file = path_to_zip_file
        self.password = password

    def __enter__(self):
        self.zip_file = zipfile.ZipFile(self.path_to_zip_file, 'w', zipfile.ZIP_DEFLATED)
        self.zip_file.setpassword(self.password)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.zip_file.close()

    @staticmethod
    def _relative_tree(root):
        for abs_root, dirs, files in os.walk(root):
            for file in files:
                abs_path = os.sep.join([abs_root, file])
                rel_path = abs_path[len(root) + 1:]
                yield abs_path, rel_path

    def archive(self, source_dir):
        for abs_path, rel_path in self.__class__._relative_tree(source_dir):
            self.zip_file.write(abs_path, arcname=rel_path)


def args_parse():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-i', '--input',
                        default=r'E:\Projects\Python\Switch_to_Python\switch-to-python-mp\Week_1',
                        help="Input path with destination to the directory",
                        type=str,
                        metavar='/usr/home'
                        )
    parser.add_argument('-o', '--output',
                        default=r'E:\Projects\Python\Switch_to_Python\switch-to-python-mp\week_1.zip',
                        help="Output .zip file with destination to the directory",
                        type=str,
                        metavar='/usr/home/archive.zip')
    parser.add_argument('-p', '--password',
                        default=None,
                        help="Password for the .zip file",
                        metavar='password')
    args = parser.parse_args()

    return args


def main():

    args = args_parse()

    with dir_zipper(args.output, args.password) as zipper:
        zipper.archive(args.input)


if __name__ == '__main__':
    main()
