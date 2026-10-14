
import tkinter as tk
from tkinter import ttk, messagebox

from src.scamsieve import analyze_message


# ==================== THEME ====================

BG = "#0B1020"
PANEL = "#151C2F"
INPUT_BG = "#0F172A"
BORDER = "#28344D"
TEXT = "#F1F5F9"
MUTED = "#94A3B8"
PURPLE = "#8B5CF6"
PURPLE_HOVER = "#7C3AED"
TEAL = "#2DD4BF"
RED = "#FB7185"
GREEN = "#4ADE80"


class ScamSieveGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("ScamSieve | Message Security")
        self.root.geometry("960x850")
        self.root.minsize(680, 650)
        self.root.configure(bg=BG)

        self.setup_styles()
        self.setup_ui()

        self.root.protocol("WM_DELETE_WINDOW", self.close)

    # ==================== STYLES ====================

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use("clam")

        style.configure(
            "Primary.TButton",
            background=PURPLE,
            foreground="white",
            font=("Segoe UI", 10, "bold"),
            padding=(17, 10),
            borderwidth=0,
        )

        style.map(
            "Primary.TButton",
            background=[("active", PURPLE_HOVER)],
        )

        style.configure(
            "Secondary.TButton",
            background=PANEL,
            foreground=TEXT,
            font=("Segoe UI", 10),
            padding=(15, 10),
            borderwidth=1,
        )

        style.map(
            "Secondary.TButton",
            background=[("active", BORDER)],
        )

    # ==================== MAIN INTERFACE ====================

    def setup_ui(self):
        main = tk.Frame(self.root, bg=BG)
        main.pack(fill="both", expand=True, padx=26, pady=18)

        # Header
        header = tk.Frame(main, bg=BG)
        header.pack(fill="x", pady=(0, 18))

        logo = tk.Label(
            header,
            text="S",
            bg=PURPLE,
            fg="white",
            font=("Segoe UI", 23, "bold"),
            width=3,
            pady=6,
        )
        logo.pack(side="left", padx=(0, 12))

        heading = tk.Frame(header, bg=BG)
        heading.pack(side="left", fill="x", expand=True)

        tk.Label(
            heading,
            text="ScamSieve",
            bg=BG,
            fg=TEXT,
            font=("Segoe UI", 24, "bold"),
        ).pack(anchor="w")

        tk.Label(
            heading,
            text="MESSAGE SECURITY ANALYZER",
            bg=BG,
            fg=MUTED,
            font=("Segoe UI", 9, "bold"),
        ).pack(anchor="w", pady=(2, 0))

        tk.Label(
            header,
            text="●  RULE-BASED",
            bg="#12332F",
            fg=TEAL,
            font=("Segoe UI", 9, "bold"),
            padx=12,
            pady=8,
        ).pack(side="right", anchor="n")

        # Introduction
        tk.Label(
            main,
            text="Check before you trust.",
            bg=BG,
            fg=TEXT,
            font=("Segoe UI", 17, "bold"),
        ).pack(anchor="w")

        tk.Label(
            main,
            text="Inspect a message for configured warning signs.",
            bg=BG,
            fg=MUTED,
            font=("Segoe UI", 10),
        ).pack(anchor="w", pady=(4, 13))

        # Message input card
        input_card = tk.Frame(
            main,
            bg=PANEL,
            highlightbackground=BORDER,
            highlightthickness=1,
        )
        input_card.pack(fill="x", pady=(0, 11))

        input_inner = tk.Frame(input_card, bg=PANEL)
        input_inner.pack(fill="x", padx=15, pady=12)

        tk.Label(
            input_inner,
            text="MESSAGE INPUT",
            bg=PANEL,
            fg=TEXT,
            font=("Segoe UI", 10, "bold"),
        ).pack(anchor="w", pady=(0, 8))

        self.message_input = tk.Text(
            input_inner,
            height=4,
            wrap="word",
            bg=INPUT_BG,
            fg=TEXT,
            insertbackground=TEAL,
            selectbackground=PURPLE,
            font=("Consolas", 10),
            relief="flat",
            borderwidth=0,
            padx=11,
            pady=10,
            undo=True,
        )
        self.message_input.pack(fill="x")

        tk.Label(
            input_inner,
            text="Never paste real passwords, PINs, or OTPs.",
            bg=PANEL,
            fg=MUTED,
            font=("Segoe UI", 9),
        ).pack(anchor="w", pady=(7, 0))

        # Action buttons
        actions = tk.Frame(main, bg=BG)
        actions.pack(fill="x", pady=(0, 15))

        ttk.Button(
            actions,
            text="Analyze Message  →",
            style="Primary.TButton",
            command=self.analyze,
        ).pack(side="left")

        ttk.Button(
            actions,
            text="Clear",
            style="Secondary.TButton",
            command=self.clear,
        ).pack(side="left", padx=(9, 0))

        # Report heading
        results_header = tk.Frame(main, bg=BG)
        results_header.pack(fill="x", pady=(0, 8))

        tk.Label(
            results_header,
            text="ANALYSIS REPORT",
            bg=BG,
            fg=TEXT,
            font=("Segoe UI", 11, "bold"),
        ).pack(side="left")

        self.status_label = tk.Label(
            results_header,
            text="READY",
            bg="#273449",
            fg=MUTED,
            font=("Segoe UI", 8, "bold"),
            padx=10,
            pady=5,
        )
        self.status_label.pack(side="right")

        # Summary card
        self.summary_card = tk.Frame(
            main,
            bg=PANEL,
            highlightbackground=BORDER,
            highlightthickness=1,
        )
        self.summary_card.pack(fill="x", pady=(0, 9))

        self.summary_title = tk.Label(
            self.summary_card,
            text="Ready to analyze",
            bg=PANEL,
            fg=TEXT,
            font=("Segoe UI", 12, "bold"),
        )
        self.summary_title.pack(anchor="w", padx=13, pady=(10, 3))

        self.summary_detail = tk.Label(
            self.summary_card,
            text="Your results will appear here.",
            bg=PANEL,
            fg=MUTED,
            font=("Segoe UI", 9),
            wraplength=800,
            justify="left",
        )
        self.summary_detail.pack(anchor="w", padx=13, pady=(0, 10))

        # Scrollable results area
        results_outer = tk.Frame(
            main,
            bg=BG,
            highlightbackground=BORDER,
            highlightthickness=1,
        )
        results_outer.pack(fill="both", expand=True)

        self.canvas = tk.Canvas(
            results_outer,
            bg=BG,
            highlightthickness=0,
            borderwidth=0,
        )

        scrollbar = ttk.Scrollbar(
            results_outer,
            orient="vertical",
            command=self.canvas.yview,
        )

        self.results_frame = tk.Frame(self.canvas, bg=BG)

        self.results_window = self.canvas.create_window(
            (0, 0),
            window=self.results_frame,
            anchor="nw",
        )

        self.results_frame.bind(
            "<Configure>",
            self.update_scroll_region,
        )

        self.canvas.bind(
            "<Configure>",
            self.resize_results_frame,
        )

        self.canvas.configure(
            yscrollcommand=scrollbar.set,
        )

        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.canvas.bind("<Enter>", self.enable_mousewheel)
        self.canvas.bind("<Leave>", self.disable_mousewheel)

        # Footer
        tk.Label(
            main,
            text="SCAMSIEVE  •  EDUCATIONAL SECURITY TOOL",
            bg=BG,
            fg=MUTED,
            font=("Segoe UI", 8, "bold"),
        ).pack(anchor="w", pady=(10, 0))

        self.show_empty_state()

    # ==================== SCROLLING ====================

    def update_scroll_region(self, event=None):
        self.canvas.configure(
            scrollregion=self.canvas.bbox("all")
        )

    def resize_results_frame(self, event):
        self.canvas.itemconfigure(
            self.results_window,
            width=event.width,
        )

    def enable_mousewheel(self, event=None):
        self.canvas.bind_all(
            "<MouseWheel>",
            self.on_mousewheel,
        )

    def disable_mousewheel(self, event=None):
        self.canvas.unbind_all("<MouseWheel>")

    def on_mousewheel(self, event):
        if event.delta:
            self.canvas.yview_scroll(
                int(-event.delta / 120),
                "units",
            )

    # ==================== REPORT COMPONENTS ====================

    def clear_results(self):
        for widget in self.results_frame.winfo_children():
            widget.destroy()

        self.canvas.yview_moveto(0)

    def add_result_card(self, title, phrases):
        card = tk.Frame(
            self.results_frame,
            bg=PANEL,
            highlightbackground=BORDER,
            highlightthickness=1,
        )
        card.pack(fill="x", padx=10, pady=(10, 0))

        tk.Label(
            card,
            text=title.upper(),
            bg=PANEL,
            fg=PURPLE,
            font=("Segoe UI", 10, "bold"),
        ).pack(anchor="w", padx=12, pady=(8, 3))

        tk.Label(
            card,
            text="Matched phrases",
            bg=PANEL,
            fg=MUTED,
            font=("Segoe UI", 9),
        ).pack(anchor="w", padx=12)

        for phrase in phrases:
            tk.Label(
                card,
                text=f"•  {phrase}",
                bg=PANEL,
                fg=TEAL,
                font=("Consolas", 10),
            ).pack(anchor="w", padx=14, pady=1)

        tk.Frame(
            card,
            bg=PANEL,
            height=6,
        ).pack()

    def show_empty_state(self):
        self.clear_results()

        tk.Label(
            self.results_frame,
            text="◈",
            bg=BG,
            fg=PURPLE,
            font=("Segoe UI", 28),
        ).pack(pady=(22, 5))

        tk.Label(
            self.results_frame,
            text="Your analysis starts here",
            bg=BG,
            fg=TEXT,
            font=("Segoe UI", 12, "bold"),
        ).pack()

        tk.Label(
            self.results_frame,
            text=(
                "Paste a message above and click Analyze Message.\n"
                "ScamSieve checks configured phrases, not actual intent."
            ),
            bg=BG,
            fg=MUTED,
            font=("Segoe UI", 9),
            justify="center",
            wraplength=600,
        ).pack(pady=(7, 20))

        self.summary_title.configure(
            text="Ready to analyze"
        )
        self.summary_detail.configure(
            text="No message has been analyzed yet."
        )

        self.set_status(
            "READY",
            MUTED,
            "#273449",
        )

    def set_status(self, text, foreground, background):
        self.status_label.configure(
            text=text,
            fg=foreground,
            bg=background,
        )

    # ==================== ANALYSIS ====================

    def analyze(self):
        message = self.message_input.get("1.0", "end-1c")

        try:
            findings = analyze_message(message)
        except (TypeError, ValueError) as error:
            messagebox.showerror(
                "Input Error",
                str(error),
                parent=self.root,
            )
            return

        self.clear_results()

        if not findings:
            self.summary_title.configure(
                text="No configured warning signs found"
            )
            self.summary_detail.configure(
                text=(
                    "This does not establish that the message is safe."
                )
            )

            self.set_status(
                "NO MATCHES",
                GREEN,
                "#12332F",
            )

            tk.Label(
                self.results_frame,
                text="No configured phrases matched.",
                bg=PANEL,
                fg=GREEN,
                font=("Segoe UI", 11, "bold"),
                padx=15,
                pady=15,
            ).pack(fill="x", padx=10, pady=10)

            tk.Label(
                self.results_frame,
                text=(
                    "ScamSieve may miss suspicious messages that use "
                    "unfamiliar wording or patterns."
                ),
                bg=BG,
                fg=MUTED,
                font=("Segoe UI", 9),
                wraplength=650,
                justify="left",
            ).pack(anchor="w", padx=12, pady=7)

            return

        category_count = len(findings)

        phrase_count = sum(
            len(item["matched_phrases"])
            for item in findings
        )

        category_word = (
            "category" if category_count == 1 else "categories"
        )

        self.summary_title.configure(
            text=(
                f"{category_count} warning {category_word} detected"
            )
        )

        self.summary_detail.configure(
            text=(
                f"{phrase_count} configured phrase matches found. "
                "Review the findings below."
            )
        )

        self.set_status(
            "REVIEW MESSAGE",
            RED,
            "#3B202B",
        )

        for finding in findings:
            self.add_result_card(
                finding["category"],
                finding["matched_phrases"],
            )

        tk.Label(
            self.results_frame,
            text=(
                "These findings are warning signals, not proof of fraud. "
                "Verify suspicious requests independently."
            ),
            bg=BG,
            fg=MUTED,
            font=("Segoe UI", 9),
            wraplength=650,
            justify="left",
        ).pack(anchor="w", padx=12, pady=12)

        self.canvas.yview_moveto(0)

    # ==================== ACTIONS ====================

    def clear(self):
        self.message_input.delete("1.0", tk.END)
        self.show_empty_state()
        self.message_input.focus_set()

    def close(self):
        self.disable_mousewheel()
        self.root.destroy()


def main():
    root = tk.Tk()
    ScamSieveGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
