#!/usr/bin/env python3

from aeneas.executetask import ExecuteTask
from aeneas.task import Task
from aeneas.tools.execute_task import ExecuteTaskCLI
import sys
import os

def sync_audio_text(audio_path, text_path, output_path):
    config_string = u"task_language=eng|is_text_type=plain|os_task_file_format=srt"
    task = Task(config_string=config_string)
    task.audio_file_path_absolute = audio_path
    task.text_file_path_absolute = text_path
    task.sync_map_file_path_absolute = output_path

    ExecuteTask(task).execute()
    task.output_sync_map_file()

def main():
    if len(sys.argv) != 4:
        print("Usage: python3 karaoke-generator.py <audio_file.mp3> <text_file.txt> <output_file.srt>")
        sys.exit(1)
    
    audio_file = sys.argv[1]
    text_file = sys.argv[2]
    output_file = sys.argv[3]
    
    if not os.path.exists(audio_file):
        print(f"Error: Audio file '{audio_file}' not found")
        sys.exit(1)
    if not os.path.exists(text_file):
        print(f"Error: Text file '{text_file}' not found")
        sys.exit(1)
        
    try:
        sync_audio_text(audio_file, text_file, output_file)
        print(f"Successfully created SRT file: {output_file}")
    except Exception as e:
        print(f"Error during synchronization: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
