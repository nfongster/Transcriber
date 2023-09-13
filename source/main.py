import tkinter as tk
from tkinter import filedialog, messagebox
from movReader import MOV_EXTENSION, WAV_EXTENSION
from mainScript import main_script


BACKGROUND_COLOR = "#57749B"
BUTTON_COLOR = "gray"
TRANSCRIBE_COLOR = "red"

channel_dict = {
    0: "Left",
    1: "Right"
}


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


def update_diagnostic_log(text, diagnostic_log, print_to_console=True):
    if print_to_console:
        print(text + "\n")
    diagnostic_log.config(state="normal")
    diagnostic_log.insert(tk.END, text + "\n")
    diagnostic_log.config(state="disabled")


def transcribe(source_file: str, output_dir: str, model_dir: str, diagnostic_log, channel: int):
    if (source_file is None) or (output_dir is None) or (model_dir is None) \
            or (source_file == '') or (output_dir == '') or (model_dir == ''):
        messagebox.showerror("Error",
                             "The source file, output directory, and model directory must all be specified!")
        return

    update_diagnostic_log(f"Source file: {source_file}", diagnostic_log)
    update_diagnostic_log(f"Output directory: {output_dir}", diagnostic_log)
    update_diagnostic_log(f"Model directory: {model_dir}\n", diagnostic_log)
    update_diagnostic_log(f"Beginning transcription ({channel_dict[channel]} channel)...\n", diagnostic_log)

    try:
        main_script(source_file, output_dir, model_dir, channel)

    except Exception as ex:
        update_diagnostic_log(f"Exception during transcription: {ex}", diagnostic_log)
        update_diagnostic_log("Failed transcription attempt.", diagnostic_log)

    finally:
        update_diagnostic_log("Transcription attempt complete.", diagnostic_log)


def main():
    window = tk.Tk()
    window.geometry("700x350")
    window.resizable(False, False)
    window.title("Transcriber")
    window.configure(bg=BACKGROUND_COLOR)

    window_frame = tk.Frame()
    window_frame.config(bg=BACKGROUND_COLOR)

    source_file_frame = tk.Frame(master=window_frame, bg=BACKGROUND_COLOR)
    output_dir_frame = tk.Frame(master=window_frame, bg=BACKGROUND_COLOR)
    model_dir_frame = tk.Frame(master=window_frame, bg=BACKGROUND_COLOR)
    transcribe_btn_frame = tk.Frame(master=window_frame, bg=BACKGROUND_COLOR)
    diagnostic_log_frame = tk.Frame(master=window_frame, bg=BACKGROUND_COLOR)

    ety_source_file = tk.Entry(master=source_file_frame, state="readonly", width=60)
    btn_source_file = tk.Button(master=source_file_frame,
                                text="Source File (*.wav or *.mov)",
                                width=15,
                                bg=BUTTON_COLOR,
                                command=lambda: open_file(ety_source_file))
    ety_source_file.pack(padx=5, pady=5, fill=tk.BOTH, side=tk.RIGHT, expand=True)
    btn_source_file.pack(padx=5, pady=5, fill=tk.BOTH, side=tk.LEFT, expand=True)

    ety_output_dir = tk.Entry(master=output_dir_frame, state="readonly", width=60)
    btn_output_dir = tk.Button(master=output_dir_frame,
                               text="Output Directory",
                               width=15,
                               bg=BUTTON_COLOR,
                               command=lambda: open_folder(ety_output_dir))
    ety_output_dir.pack(padx=5, pady=5, fill=tk.BOTH, side=tk.RIGHT, expand=True)
    btn_output_dir.pack(padx=5, pady=5, fill=tk.BOTH, side=tk.LEFT, expand=True)

    ety_model_dir = tk.Entry(master=model_dir_frame, state="readonly", width=60)
    btn_model_dir = tk.Button(master=model_dir_frame,
                              text="Model Directory",
                              width=15,
                              bg=BUTTON_COLOR,
                              command=lambda: open_folder(ety_model_dir))

    ety_model_dir.pack(padx=5, pady=5, fill=tk.BOTH, side=tk.RIGHT, expand=True)
    btn_model_dir.pack(padx=5, pady=5, fill=tk.BOTH, side=tk.LEFT, expand=True)

    channel = tk.IntVar(value=0)  # 0 for left, 1 for right

    radio_button_label = tk.Label(master=transcribe_btn_frame,
                                  text="Channel (if stereo):",
                                  bg=BACKGROUND_COLOR)
    left_channel_radio_btn = tk.Radiobutton(master=transcribe_btn_frame,
                                            text="Left",
                                            bg=BACKGROUND_COLOR,
                                            variable=channel,
                                            value=0)

    right_channel_radio_btn = tk.Radiobutton(master=transcribe_btn_frame,
                                             text="Right",
                                             bg=BACKGROUND_COLOR,
                                             variable=channel,
                                             value=1)

    btn_transcribe = tk.Button(master=transcribe_btn_frame,
                               text="Transcribe",
                               width=15,
                               bg=TRANSCRIBE_COLOR,
                               command=lambda: transcribe(ety_source_file.get(),
                                                          ety_output_dir.get(),
                                                          ety_model_dir.get(),
                                                          diagnostic_log,
                                                          channel.get()))
    radio_button_label.pack(padx=5, pady=5, side="left")
    left_channel_radio_btn.pack(padx=5, pady=5, side="left")
    right_channel_radio_btn.pack(padx=5, pady=5, side="left")
    btn_transcribe.pack(padx=5, pady=5)

    diagnostic_log = tk.Text(master=diagnostic_log_frame, state="disabled", bg="black", fg="white")
    diagnostic_log.pack(fill="both", expand=True)

    source_file_frame.pack(padx=5, pady=5, fill=tk.X)
    output_dir_frame.pack(padx=5, pady=5, fill=tk.X)
    model_dir_frame.pack(padx=5, pady=5, fill=tk.X)
    transcribe_btn_frame.pack(padx=5, pady=5, fill=tk.X)
    diagnostic_log_frame.pack(padx=5, pady=5, fill=tk.X)
    window_frame.pack(padx=5, pady=5, fill=tk.BOTH, side=tk.LEFT, expand=True)

    window.mainloop()


if __name__ == '__main__':
    main()
