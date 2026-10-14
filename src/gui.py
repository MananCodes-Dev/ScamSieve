
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.scrolledtext import ScrolledText

from src.scamsieve import analyze_message


class ScamSieveGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("ScamSieve | Message Analyzer")
        self.root.geometry("760x680")
        self.root.minsize(600, 550)

        self.setup_ui()

    def setup_ui(self):
        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.pack(fill="both", expand=True)

        title = ttk.Label(
            main_frame,
            text="ScamSieve",
            font=("Segoe UI", 24, "bold"),
        )
        title.pack(anchor="w")

        subtitle = ttk.Label(
            main_frame,
            text="Analyze messages for configured warning signs.",
            font=("Segoe UI", 10),
        )
        subtitle.pack(anchor="w", pady=(2, 15))

        input_label = ttk.Label(
            main_frame,
            text="Paste your message:",
            font=("Segoe UI", 11, "bold"),
        )
        input_label.pack(anchor="w", pady=(0, 6))

        self.message_input = ScrolledText(
            main_frame,
            height=8,
            wrap="word",
            font=("Segoe UI", 11),
        )
        self.message_input.pack(fill="x", pady=(0, 12))

        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill="x", pady=(0, 15))

        analyze_button = ttk.Button(
            button_frame,
            text="Analyze Message",
            command=self.analyze,
        )
        analyze_button.pack(side="left")

        clear_button = ttk.Button(
            button_frame,
            text="Clear",
            command=self.clear,
        )
        clear_button.pack(side="left", padx=(10, 0))

        results_label = ttk.Label(
            main_frame,
            text="Analysis Results:",
            font=("Segoe UI", 11, "bold"),
        )
        results_label.pack(anchor="w", pady=(0, 6))

        self.results_output = ScrolledText(
            main_frame,
            height=12,
            wrap="word",
            font=("Segoe UI", 10),
            state="disabled",
        )
        self.results_output.pack(fill="both", expand=True)

        disclaimer = ttk.Label(
            main_frame,
            text=(
                "Important: ScamSieve is a basic rule-based tool. "
                "It cannot confirm whether a message or link is safe."
            ),
            wraplength=700,
            font=("Segoe UI", 9),
        )
        disclaimer.pack(anchor="w", pady=(12, 0))

    def show_results(self, text):
        self.results_output.configure(state="normal")
        self.results_output.delete("1.0", tk.END)
        self.results_output.insert(tk.END, text)
        self.results_output.configure(state="disabled")

    def analyze(self):
        message = self.message_input.get("1.0", "end-1c")

        try:
            findings = analyze_message(message)
        except (TypeError, ValueError) as error:
            messagebox.showerror("Input Error", str(error))
            return

        if not findings:
            result_text = (
                "No configured warning signs detected.\n\n"
                "This does NOT mean the message is safe. "
                "The tool only checks its configured rules."
            )
        else:
            lines = ["Warning signs detected:\n"]

            for finding in findings:
                lines.append(f"Category: {finding['category']}")
                lines.append("Matched phrases:")

                for phrase in finding["matched_phrases"]:
                    lines.append(f"  - {phrase}")

                lines.append("")

            lines.append(
                "Reminder: These are warning signals, not proof of a scam."
            )

            result_text = "\n".join(lines)

        self.show_results(result_text)

    def clear(self):
        self.message_input.delete("1.0", tk.END)
        self.show_results("")


def main():
    root = tk.Tk()
    ScamSieveGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
