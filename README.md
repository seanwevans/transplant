# transplant

Recreate directory structures from `tree`'s output.

## Overview

`transplant` is a command-line utility that reads the formatted output of the `tree` command and recreates the directory structure in a specified location. This is useful for quickly rebuilding directory hierarchies without having to manually create each directory and file.

## Installation

Clone this repository and make the script executable:

```bash
git clone https://github.com/yourusername/transplant.git
cd transplant
chmod +x transplant
```

You can also add it to your PATH for system-wide access.

## Prerequisites

- Python 3.6+
- The script has no external dependencies beyond the Python standard library

## Usage

Basic usage:

```bash
./transplant TREE_OUTPUT DEST_DIR
```

Where:
- `TREE_OUTPUT` is a text file containing the output of the `tree` command
- `DEST_DIR` is the directory where you want to recreate the structure

### Options

```
-d, --dry-run   Don't touch the filesystem—just report what would be done
-v, --verbose   Print each path as it is (or would be) created
    --ascii     Parse ASCII tree output instead of Unicode
-h, --help      Show help message and exit
```

## Examples

1. Generate a tree representation of a directory structure:

```bash
tree /path/to/source > directory_structure.txt
```

2. Recreate that structure in a new location:

```bash
./transplant directory_structure.txt /path/to/destination
```

3. Do a dry run to see what would happen without modifying the filesystem:

```bash
./transplant directory_structure.txt --dry-run
```

4. Verbose output showing each path as it's created:

```bash
./transplant directory_structure.txt /path/to/destination --verbose
```

## License

[MIT License](LICENSE)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
