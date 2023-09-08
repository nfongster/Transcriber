import tkinter as tk
from tkinter import filedialog
from movReader import MOV_EXTENSION, WAV_EXTENSION


def main():
    window = tk.Tk()
    window.geometry("700x350")
    window.resizable(False, False)
    window.title("Transcriber")

    left_frame = tk.Frame(bg="blue")
    right_frame = tk.Frame(bg="green")

    source_file_frame = tk.Frame(master=left_frame)
    output_dir_frame = tk.Frame(master=left_frame)
    model_dir_frame = tk.Frame(master=left_frame)
    transcribe_btn_frame = tk.Frame(master=left_frame)

    def open_file():
        file_path = filedialog.askopenfilename(
            filetypes=[("WAV Files", f"*{WAV_EXTENSION}"), ("MOV Files", f"*{MOV_EXTENSION}")]
        )
        if file_path:
            ety_source_file.configure(state="normal")
            ety_source_file.delete(0, tk.END)
            ety_source_file.insert(0, file_path)
            ety_source_file.configure(state="readonly")

    def open_folder():
        folder_path = filedialog.askdirectory()
        if folder_path:
            ety_output_dir.configure(state="normal")
            ety_output_dir.delete(0, tk.END)
            ety_output_dir.insert(0, folder_path)
            ety_output_dir.configure(state="readonly")

    btn_source_file = tk.Button(master=source_file_frame, text="File location (*.wav or *.mov)", command=open_file)
    ety_source_file = tk.Entry(master=source_file_frame, state="readonly", width=60)

    btn_output_dir = tk.Button(master=output_dir_frame, text="Output directory", command=open_folder)
    ety_output_dir = tk.Entry(master=output_dir_frame, state="readonly", width=60)

    # label2 = tk.Label(master=output_dir_frame, text="Second Label")
    # label3 = tk.Label(master=model_dir_frame, text="Third Label")
    # btn_transcribe = tk.Button(master=transcribe_btn_frame, text="Transcribe")

    btn_source_file.pack(padx=5, pady=5, fill=tk.BOTH, side=tk.LEFT, expand=True)
    ety_source_file.pack(padx=5, pady=5, fill=tk.BOTH, side=tk.RIGHT, expand=True)
    btn_output_dir.pack(padx=5, pady=5, fill=tk.BOTH, side=tk.LEFT, expand=True)
    ety_output_dir.pack(padx=5, pady=5, fill=tk.BOTH, side=tk.RIGHT, expand=True)
    # btn_transcribe.pack()

    label4 = tk.Label(master=right_frame, text="Fourth Label")
    label4.pack()

    source_file_frame.pack(padx=5, pady=5, fill=tk.X)
    output_dir_frame.pack(padx=5, pady=5, fill=tk.X)
    left_frame.pack(padx=5, pady=5, fill=tk.BOTH, side=tk.LEFT, expand=True)
    right_frame.pack(padx=5, pady=5, fill=tk.BOTH, side=tk.RIGHT, expand=True)

    window.mainloop()


if __name__ == '__main__':
    main()
