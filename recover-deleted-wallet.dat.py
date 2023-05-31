#!/usr/bin/env python3
# recover deleted wallet.dat from a disk image
# Made in conversation with ChatGPT / GPT-4
# 2023-05-12 tzatko
#

import sys
import os
import binascii

def search_for_wallet(image_path, start_position=0):
    wallet_data_signatures = [b'\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x62\x31\x05\x00']  # BDB 1.85 magic bytes
    buffer_size = 64 * 1024

    found_wallets = 0

    try:
        with open(image_path, "rb") as img_file:
            file_size = os.path.getsize(image_path)
            position = start_position
            overlap = max(len(sig) for sig in wallet_data_signatures) - 1

            img_file.seek(position)
            buffer = img_file.read(buffer_size + overlap)

            last_percentage = 0

            while buffer:
                for wallet_data_signature in wallet_data_signatures:
                    signature_position = buffer.find(wallet_data_signature)

                    if signature_position != -1:
                        found_wallets += 1
                        wallet_file_path = f"recovered_wallet_{found_wallets}.dat"
                        print(f"Found wallet data at position {position + signature_position}. Saving to {wallet_file_path}...")

                        img_file.seek(position + signature_position)
                        wallet_data = img_file.read(1024 * 1024)
                        with open(wallet_file_path, "wb") as wallet_file:
                            wallet_file.write(wallet_data)

                position += buffer_size
                img_file.seek(position)
                buffer = img_file.read(buffer_size + overlap)

                # Print search progress
                progress_percentage = (position / file_size) * 100
                if abs(progress_percentage - last_percentage) >= 0.1:
                    print(f"Search progress: {progress_percentage:.2f}% ({position / (1024 * 1024 * 1024):.2f} of {file_size / (1024 * 1024 * 1024):.2f} GB), wallets found: {found_wallets}")
                    last_percentage = progress_percentage

    except Exception as e:
        print(f"Error processing disk image: {str(e)}")

    if found_wallets == 0:
        print("No wallet.dat files found.")

def parse_start_position(arg):
    if arg.endswith('%'):
        return int(float(arg.strip('%')) / 100 * os.path.getsize(sys.argv[1]))
    if arg.lower().endswith('gb'):
        return int(float(arg.strip('GBgb')) * 1024 * 1024 * 1024)
    return int(arg)

if __name__ == "__main__":
    if len(sys.argv) not in (2, 3):
        print("Usage: python recover_wallet_raw.py <image_path> [<start_position>]")
    else:
        start_position = 0
        if len(sys.argv) == 3:
            start_position = parse_start_position(sys.argv[2])
        search_for_wallet(sys.argv[1], start_position)

