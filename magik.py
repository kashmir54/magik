import argparse
import sys


magic_bytes = {

	'ico': 	{'b': [b'\x00\x00\x01\x00']},
	'icns': {'b': [b'\x69\x63\x6e\x73']},
	'png': 	{'b': [b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A']},
	'plist': {'b': [b'\x62\x70\x6C\x69\x73\x74']},
	'gif': {'b': [b'\x47\x49\x46\x38\x37\x61']},
	'tif': {'b': [b'\x49\x49\x2A\x00']},
	'cr2': {'b': [b'\x49\x49\x2A\x00\x10\x00\x00\x00\x43\x52']},
	'jpg': {'b': [b'\xFF\xD8\xFF\xDB', b'\xFF\xD8\xFF\xE0\x00\x10\x4A\x46\x49\x46\x00\x01', b'\xFF\xD8\xFF\xEE']},
	'zip': {'b': [b'\x50\x4B\x03\x04', b'\x50\x4B\x05\x06', b'\x50\x4B\x07\x08']},
	'rar': {'b': [b'\x52\x61\x72\x21\x1A\x07\x00']},
	'elf': {'b': [b'\x7F\x45\x4C\x46']},
	'class': {'b': [b'\xCA\xFE\xBA\xBE']},
	'utf8': {'b': [b'\xEF\xBB\xBF']},
	'utf16le': {'b': [b'\xFF\xFE']},
	'utf16be': {'b': [b'\xFE\xFF']},
	'utf32le': {'b': [b'\xFF\xFE\x00\x00']},
	'utf32be': {'b': [b'\x00\x00\xFE\xFF']},
	'pdf': {'b': [b'\x25\x50\x44\x46\x2D', b'\xDF\xBF\x34\xEB\xCE']},
	'wma': {'b': [b'\x30\x26\xB2\x75\x8E\x66\xCF\x11\xA6\xD9\x00\xAA\x00\x62\xCE\x6C']},
	'ogg': {'b': [b'\x4F\x67\x67\x53']},
	'mp3': {'b': [b'\xFF\xFB', b'\xFF\xF3', b'\xFF\xF2', b'\x49\x44\x33']},
	'tar': {'b': [b'\x75\x73\x74\x61\x72\x00\x30\x30', b'\x75\x73\x74\x61\x72\x20\x20\x00']},
	'bmp': {'b': [b'\x42\x4D']},
	'doc': {'b': [b'\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1']},
	'xls': {'b': [b'\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1']},
	'dex': {'b': [b'\x64\x65\x78\x0A\x30\x33\x35\x00']},
	'vmdk': {'b': [b'\x4B\x44\x4D']},
	'dmg': {'b': [b'\x6B\x6F\x6C\x79']},
	'xar': {'b': [b'\x78\x61\x72\x21']},
	'7z': {'b': [b'\x37\x7A\xBC\xAF\x27\x1C']},
	'gz': {'b': [b'\x1F\x8B']},
	'xz': {'b': [b'\xFD\x37\x7A\x58\x5A\x00']},
	'mkv': {'b': [b'\x1A\x45\xDF\xA3']},
	'woff': {'b': [b'\x77\x4F\x46\x46']},
	'xml': {'b': [b'\x3C\x3F\x78\x6D\x6C\x20']},
	'wasm': {'b': [b'\x00\x61\x73\x6D']},
	'deb': {'b': [b'\x21\x3C\x61\x72\x63\x68\x3E\x0A']},
	'rtf': {'b': [b'\x7B\x5C\x72\x74\x66\x31']},
	'mp4': {'b': [b'\x66\x74\x79\x70\x69\x73\x6F\x6D']},
	'eml': {'b': [b'\x52\x65\x63\x65\x69\x76\x65\x64\x3A']},
	'flv': {'b': [b'\x46\x4C\x56']}
}


def add_magic(filename, target_magic, option=0):

	current_file = ''
	with open(filename, 'rb') as in_file:
		current_file = in_file.read()

	new_payload = magic_bytes[target_magic]['b'][option] + current_file

	new_filename = 'mk_' + filename
	with open(new_filename, 'wb') as out_file:
		out_file.write(new_payload)
		

if __name__ == '__main__':

	parser = argparse.ArgumentParser(epilog="Select your input file and the target magic bytes", formatter_class=argparse.RawTextHelpFormatter)
	parser.add_argument("filename", nargs='?', type=str,
						help="Target filename")
	parser.add_argument("-m", "--magic", action="store",
						help="Extension for selecting corresponding magic bytes")
	parser.add_argument("-o", "--option", action="store",
						help="Option payload for multiple options magic bytes")

	args = parser.parse_args()

	option, extension, filename = 0,'',''

	if args.magic:
		extension = args.magic
	if args.filename:
		filename = args.filename
	if args.option:
		option = args.option

	add_magic(filename, extension, option)