import tkinter as tk
from tkinter import filedialog, messagebox
import base64
import os
from PIL import Image, ImageTk
import io

CHUNK_SIZE = 1024 * 1024  # 1MB chunks

class Base64Simulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Base64 Encoding Simulation (Not Security)")
        self.root.geometry("900x700")

        self.image_label = None

        # Encode section
        tk.Label(root, text="1. Encode File to Base64", font=("Arial", 12, "bold")).pack(pady=5)
        tk.Button(root, text="Select File & Encode", command=self.encode_file).pack()

        self.encode_output = tk.Text(root, height=8)
        self.encode_output.pack(fill="x", padx=10, pady=5)

        # Decode section
        tk.Label(root, text="2. Decode Base64 ", font=("Arial", 12, "bold")).pack(pady=5)

        self.decode_input = tk.Text(root, height=8)
        self.decode_input.pack(fill="x", padx=10, pady=5)

        tk.Button(root, text="Decode & Display", command=self.decode_and_display).pack(pady=5)

        # Image preview area
        self.preview_frame = tk.LabelFrame(root, text="Decoded Image Preview")
        self.preview_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.preview_label = tk.Label(self.preview_frame, text="No image decoded yet")
        self.preview_label.pack()

        self.status = tk.Label(root, text="Ready", fg="green")
        self.status.pack(pady=5)

    def encode_file(self):
        file_path = filedialog.askopenfilename()
        if not file_path:
            return

        self.encode_output.delete("1.0", tk.END)
        self.decode_input.delete("1.0", tk.END)

        try:
            with open(file_path, "rb") as f:
                encoded_chunks = []
                while chunk := f.read(CHUNK_SIZE):
                    encoded_chunks.append(base64.b64encode(chunk).decode())

            encoded_data = "".join(encoded_chunks)
            self.encode_output.insert(tk.END, encoded_data)
            self.decode_input.insert(tk.END, encoded_data)

            self.status.config(
                text=f"Encoded successfully | Original size: {os.path.getsize(file_path)} bytes",
                fg="blue"
            )

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def decode_and_display(self):
        base64_data = self.decode_input.get("1.0", tk.END).strip()
        if not base64_data:
            messagebox.showwarning("Warning", "Paste Base64 data first")
            return

        try:
            decoded_bytes = b""
            for i in range(0, len(base64_data), CHUNK_SIZE):
                decoded_bytes += base64.b64decode(base64_data[i:i + CHUNK_SIZE])

            # Try displaying as image
            try:
                image = Image.open(io.BytesIO(decoded_bytes))
                image.thumbnail((500, 400))

                self.tk_image = ImageTk.PhotoImage(image)
                self.preview_label.config(image=self.tk_image, text="")
                self.preview_label.image = self.tk_image

                self.status.config(
                    text="Decoded successfully → Image displayed (No key required)",
                    fg="red"
                )

            except Exception:
                # Not an image → save file
                save_path = filedialog.asksaveasfilename(defaultextension=".bin")
                if save_path:
                    with open(save_path, "wb") as f:
                        f.write(decoded_bytes)

                    self.status.config(
                        text="Decoded successfully → File saved (No key required)",
                        fg="red"
                    )

        except Exception:
            messagebox.showerror("Error", "Invalid Base64 data")

# Run app
root = tk.Tk()
app = Base64Simulator(root)
root.mainloop()
