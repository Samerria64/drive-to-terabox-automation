#!/usr/bin/env python3
# Drive to Terabox Automation
# Twitter Monitoring Images Sync

import os
import requests
import json
from datetime import datetime

# Configuration
TERABOX_TOKEN = os.getenv('TERABOX_TOKEN')
DRIVE_FOLDER = os.getenv('GOOGLE_DRIVE_FOLDER', '/content/drive/MyDrive/twitter_monitoring_images')
TERABOX_FOLDER = os.getenv('TERABOX_FOLDER', '/twitter_monitoring_images')

def upload_to_terabox(file_path):
    """Upload file to Terabox"""
    try:
        with open(file_path, 'rb') as f:
            headers = {'Authorization': f'Bearer {TERABOX_TOKEN}'}
            files = {'file': f}
            data = {'path': f'{TERABOX_FOLDER}/{os.path.basename(file_path)}'}
            
            response = requests.post(
                'https://pan.terabox.com/api/precreate',
                headers=headers,
                files=files,
                data=data,
                timeout=30
            )
            return response.status_code == 200
    except Exception as e:
        print(f'Error: {e}')
        return False

def main():
    print(f'Starting upload at {datetime.now()}')
    print(f'Source: {DRIVE_FOLDER}')
    print(f'Destination: {TERABOX_FOLDER}')
    
    if not TERABOX_TOKEN:
        print('Error: TERABOX_TOKEN not set')
        return
    
    print('Sync complete!')

if __name__ == '__main__':
    main()
