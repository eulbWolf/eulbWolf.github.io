import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from functools import partial
from modifytemps import runall  # Make sure to replace 'your_module_name' with the actual name of the module containing your functions

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("HTML Modifier App")
        
        self.template_path_label = tk.Label(root, text="Template HTML File:")
        self.template_path_label.pack()

        self.template_path_entry = tk.Entry(root, width=50)
        self.template_path_entry.pack()

        self.template_browse_button = tk.Button(root, text="Browse", command=partial(self.browse_file, self.template_path_entry))
        self.template_browse_button.pack()

        self.output_path_label = tk.Label(root, text="Output HTML File:")
        self.output_path_label.pack()

        self.output_path_entry = tk.Entry(root, width=50)
        self.output_path_entry.pack()

        self.output_browse_button = tk.Button(root, text="Browse", command=partial(self.browse_file, self.output_path_entry))
        self.output_browse_button.pack()

        self.run_button = tk.Button(root, text="Run", command=self.run_modification)
        self.run_button.pack()

    def browse_file(self, entry):
        file_path = filedialog.askopenfilename(filetypes=[("HTML Files", "*.html")])
        entry.delete(0, tk.END)
        entry.insert(0, file_path)

    def run_modification(self):
        template_path = self.template_path_entry.get()
        output_path = self.output_path_entry.get()

        if not template_path or not output_path:
            messagebox.showerror("Error", "Please provide both template and output file paths.")
            return

        try:
            runall(template_path, output_path)
            messagebox.showinfo("Success", "HTML modification and writing completed successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

