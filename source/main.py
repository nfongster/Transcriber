import tkinter as tk
from tkinter import filedialog
from movReader import MOV_EXTENSION, WAV_EXTENSION
from mainScript import main_script


def open_file(entry):
    file_path = filedialog.askopenfilename(
        filetypes=[("WAV Files", f"*{WAV_EXTENSION}"), ("MOV Files", f"*{MOV_EXTENSION}")]
    )
    if file_path:
        entry.configure(state="normal")
        entry.delete(0, tk.END)
        entry.insert(0, file_path)
        entry.configure(state="readonly")


def open_folder(entry):
    folder_path = filedialog.askdirectory()
    if folder_path:
        entry.configure(state="normal")
        entry.delete(0, tk.END)
        entry.insert(0, folder_path)
        entry.configure(state="readonly")


def transcribe(source_file: str, output_dir: str, model_dir: str):
    print(f"Source file: {source_file}")
    print(f"Output directory: {output_dir}")
    print(f"Model directory: {model_dir}\n")
    print("Transcribing...\n")
    main_script(source_file, output_dir, model_dir)


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

    ety_source_file = tk.Entry(master=source_file_frame, state="readonly", width=60)
    btn_source_file = tk.Button(master=source_file_frame,
                                text="File location (*.wav or *.mov)",
                                command=lambda: open_file(ety_source_file))
    ety_source_file.pack(padx=5, pady=5, fill=tk.BOTH, side=tk.RIGHT, expand=True)
    btn_source_file.pack(padx=5, pady=5, fill=tk.BOTH, side=tk.LEFT, expand=True)

    ety_output_dir = tk.Entry(master=output_dir_frame, state="readonly", width=60)
    btn_output_dir = tk.Button(master=output_dir_frame,
                               text="Output directory",
                               command=lambda: open_folder(ety_output_dir))
    ety_output_dir.pack(padx=5, pady=5, fill=tk.BOTH, side=tk.RIGHT, expand=True)
    btn_output_dir.pack(padx=5, pady=5, fill=tk.BOTH, side=tk.LEFT, expand=True)

    ety_model_dir = tk.Entry(master=model_dir_frame, state="readonly", width=60)
    btn_model_dir = tk.Button(master=model_dir_frame,
                              text="Model directory",
                              command=lambda: open_folder(ety_model_dir))

    ety_model_dir.pack(padx=5, pady=5, fill=tk.BOTH, side=tk.RIGHT, expand=True)
    btn_model_dir.pack(padx=5, pady=5, fill=tk.BOTH, side=tk.LEFT, expand=True)

    btn_transcribe = tk.Button(master=transcribe_btn_frame,
                               text="Transcribe",
                               command=lambda: transcribe(ety_source_file.get(),
                                                          ety_output_dir.get(),
                                                          ety_model_dir.get()))
    btn_transcribe.pack()

    label4 = tk.Label(master=right_frame, text="Fourth Label")
    label4.pack()

    source_file_frame.pack(padx=5, pady=5, fill=tk.X)
    output_dir_frame.pack(padx=5, pady=5, fill=tk.X)
    model_dir_frame.pack(padx=5, pady=5, fill=tk.X)
    transcribe_btn_frame.pack(padx=5, pady=5, fill=tk.X)
    left_frame.pack(padx=5, pady=5, fill=tk.BOTH, side=tk.LEFT, expand=True)
    right_frame.pack(padx=5, pady=5, fill=tk.BOTH, side=tk.RIGHT, expand=True)

    window.mainloop()


if __name__ == '__main__':
    main()
