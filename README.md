# Recover Deleted wallet.dat
This Python script recovers deleted Bitcoin Core wallet.dat files from a disk image. It is particularly useful for Bitcoin Core wallets created between 2009 and ~2016 using the Berkeley DB (BDB) format.

The script works by searching for the BDB 1.85 magic bytes in the disk image. It reads the image in chunks and searches for the magic bytes within each chunk, effectively performing a raw search on the disk image.

## Usage

The script can be run from the command line as follows:

```bash
python3 recover-deleted-wallet.dat.py <image_path> [<start_position>]
```

`<image_path>` is the path to the disk image file.

`<start_position>` is an optional parameter to specify the start position of the search. This can be provided as a percentage (e.g., `10%`), in gigabytes (e.g., `25GB`), or a raw byte offset (e.g., `5000000000`). If not provided, the search starts from the beginning of the file.

## Example

```bash
python3 recover-deleted-wallet.dat.py /path/to/disk/image 10%
```

The above command will start the search from the 10% position of the disk image file.

## Note

This script was developed in collaboration with ChatGPT / GPT-4 on 2023-05-12 by tzatko. The goal was to create a practical tool for recovering deleted wallet.dat files from Bitcoin Core, which could be particularly useful in digital forensics or when a wallet file has been accidentally deleted.

## Disclaimer

While this script is designed to help recover deleted wallet.dat files, success is not guaranteed. The success of the recovery depends on various factors such as the state of the disk image and whether the data has been overwritten. Always make a backup of your data and use this script at your own risk.

## The Challenge of the Empty Wallet

In the grand tradition of open source projects, here's the Bitcoin address to which you will absolutely, positively, not send a single Satoshi: bc1p8r56wjyv5cpzvr7m7mghx593eg4tz32x647v3n5z5pap4lhd9rjq7der76


This is the wallet that will remain as empty as a programmer's coffee cup at 3 AM, despite the fact that this tool just helped you recover enough Bitcoin to buy a small island.

I know how it goes: you'd have promised your firstborn and a 10% finder's fee to get those coins back. But now that you've got them, suddenly you've developed amnesia, right?

So here it is, the world's loneliest Bitcoin wallet, destined to be as forgotten as a semicolon in JavaScript: bc1p8r56wjyv5cpzvr7m7mghx593eg4tz32x647v3n5z5pap4lhd9rjq7der76

Go ahead, prove me wrong. Make my day.
