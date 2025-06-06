# transplant

Recreate directory structures from `tree`'s output.

## Overview

`transplant` is a command-line utility that reads the formatted output of the `tree` command and recreates the directory structure in a specified location. This is useful for quickly rebuilding directory hierarchies without having to manually create each directory and file.

## Installation

Install the latest version directly from the repository using `pip`:

```bash
pip install git+https://github.com/yourusername/transplant.git
```

If you prefer to isolate the tool, `pipx` works as well:

```bash
pipx install git+https://github.com/yourusername/transplant.git
```

You can still clone this repository and run the script directly if you
prefer.

## Prerequisites

- Python 3.6+
- The script has no external dependencies beyond the Python standard library

## Usage

Basic usage:

```bash
./transplant TREE_OUTPUT DEST_DIR
```

Where:
- `TREE_OUTPUT` is a text file containing the output of the `tree` command. Use
  `-` to read the listing from standard input.
- `DEST_DIR` is the directory where you want to recreate the structure

### Options

```
-d, --dry-run   Don't touch the filesystem—just report what would be done
-v, --verbose   Print each path as it is (or would be) created
    --ascii     Parse ASCII tree output instead of Unicode
    --force     Overwrite existing files when recreating the hierarchy
-V, --version   Show program's version number and exit
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

5. Read the listing from standard input:

```bash
tree /path/to/source | ./transplant - /path/to/destination
```

6. Overwrite existing files when recreating the structure:

```bash
./transplant directory_structure.txt /path/to/destination --force
```

7. Display the script version:

```bash
./transplant --version
```

## License

[MIT License](LICENSE)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
