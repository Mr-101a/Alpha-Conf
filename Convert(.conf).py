import subprocess
import os
import re
from datetime import datetime
from tkinter import Tk, Label, Button, Menu, messagebox


class ConfToCppApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CONF to C++ Generator - Alpha Team")
        self.root.geometry("700x350")
        self.root.configure(bg="#1e1e2f")

        self.create_menu()

        self.label = Label(root, text="Alpha - Convert .conf to C++", font=("Vazirmatn", 16), bg="#1e1e2f", fg="#00ffff")
        self.label.pack(pady=20)

        self.select_btn = Button(root, text="Select .conf File", command=self.select_conf_file,
                                 font=("Vazirmatn", 12), bg="#007acc", fg="white", width=30, height=2)
        self.select_btn.pack(pady=10)

        self.status_label = Label(root, text="", bg="#1e1e2f", fg="#00ff88", font=("Vazirmatn", 10))
        self.status_label.pack(pady=10)

    def create_menu(self):
        menubar = Menu(self.root, bg="#1e1e2f", fg="white", activebackground="#444", activeforeground="cyan")

        
        options_menu = Menu(menubar, tearoff=0, bg="#1e1e2f", fg="white", activebackground="#444", activeforeground="cyan")
        options_menu.add_command(label="Select .conf File  Ctrl+F", command=self.select_conf_file)
        options_menu.add_separator()
        options_menu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="Options", menu=options_menu)

        
        appearance_menu = Menu(menubar, tearoff=0, bg="#1e1e2f", fg="white", activebackground="#444", activeforeground="cyan")
        size_menu = Menu(appearance_menu, tearoff=0, bg="#1e1e2f", fg="white", activebackground="#444", activeforeground="cyan")
        sizes = {
            "Small (600x400)": "600x400",
            "Normal (800x600)": "800x600",
            "Large (1024x768)": "1024x768",
            "HD (1280x720)": "1280x720",
            "FullHD (1920x1080)": "1920x1080"
        }
        for label, size in sizes.items():
            size_menu.add_command(label=label, command=lambda s=size: self.resize_window(s))
        appearance_menu.add_cascade(label="Set Size", menu=size_menu)

        color_menu = Menu(appearance_menu, tearoff=0, bg="#1e1e2f", fg="white", activebackground="#444", activeforeground="cyan")
        colors = {
            "Dark Blue": "#1e1e2f",
            "Dark Gray": "#2e2e2e",
            "Black": "#000000",
            "White": "#ffffff"
        }
        for label, color in colors.items():
            color_menu.add_command(label=label, command=lambda c=color: self.change_background(c))
        appearance_menu.add_cascade(label="Set Color", menu=color_menu)

        menubar.add_cascade(label="Appearance", menu=appearance_menu)

        
        help_menu = Menu(menubar, tearoff=0, bg="#1e1e2f", fg="white", activebackground="#444", activeforeground="cyan")
        help_menu.add_command(label="Help", command=self.show_help)
        help_menu.add_command(label="About", command=self.show_about_info)
        menubar.add_cascade(label="Help", menu=help_menu)

        self.root.config(menu=menubar)

    def select_conf_file(self):
        try:
            file_path = subprocess.check_output([
                "env", "GDK_BACKEND=x11", "zenity", "--file-selection",
                "--title=Select .conf File", "--file-filter=*.conf"
            ]).decode("utf-8").strip()

            if file_path:
                self.status_label.config(text=f"Selected: {file_path}")
                samples = self.parse_conf_file(file_path)
                output_dir = os.path.join(os.getcwd(), "generated_cpp")
                os.makedirs(output_dir, exist_ok=True)

                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                filename = f"generated_{timestamp}.cpp"
                output_path = os.path.join(output_dir, filename)

                self.generate_ground_points_from_conf(file_path, output_path)
                self.generate_positions_cpp(samples, output_path)
                subprocess.Popen(["xdg-open", output_path])
                self.status_label.config(text=f"✅ Generated: {filename}")
        except subprocess.CalledProcessError:
            self.status_label.config(text="❌ File selection canceled.")
        except Exception as e:
            self.status_label.config(text=f"❌ Error: {str(e)}")

    def parse_conf_file(self, conf_path):
        with open(conf_path, 'r') as file:
            lines = file.readlines()

        in_samples = False
        samples = []
        current_sample = {}
        for line in lines:
            line = line.strip()

            if line.startswith("Begin Samples"):
                in_samples = True
                continue
            if line.startswith("End Samples"):
                break
            if not in_samples:
                continue

            if line.startswith("-----"):
                if current_sample:
                    samples.append(current_sample)
                current_sample = {"players": {}}
            elif line.startswith("Ball"):
                _, x, y = line.split()
                current_sample["ball"] = (float(x), float(y))
            elif re.match(r"^\d+ ", line):
                parts = line.split()
                if len(parts) >= 3:
                    try:
                        unum = int(parts[0])
                        x = float(parts[1])
                        y = float(parts[2])
                        current_sample["players"][unum] = (x, y)
                    except ValueError:
                        continue
        if current_sample:
            samples.append(current_sample)
        return samples

    def generate_ground_points_from_conf(self, conf_path, out_file):
        with open(conf_path, 'r') as file:
            lines = file.readlines()

        point_lines = []
        for i in range(len(lines)):
            line = lines[i].strip()
            if line.startswith("-----"):
                next_line = lines[i + 1].strip()
                if next_line.startswith("Ball"):
                    _, x, y = next_line.split()
                    point_lines.append((float(x), float(y)))

        with open(out_file, 'w') as f:
            f.write("// ============================================================\n")
            f.write("// Alpha Team - 2D Soccer Simulation Formation Generator \n")
            f.write("// This file contains the following functions: \n")
            f.write("//    - Alp_ground_points : Identifying the closest point on the field to the ball\n")
            f.write("//    - Alp_normal_position : Placing players based on point number\n")
            f.write("// ============================================================\n\n")
            f.write("int Bhv_BasicMove::Alp_ground_points(const rcsc::WorldModel& wm)\n{\n")
            f.write("    rcsc::Vector2D ball_pos1 = wm.ball().pos();\n")
            f.write(f"    rcsc::Vector2D point1[{len(point_lines)}];\n")
            for i, (x, y) in enumerate(point_lines):
                f.write(f"    point1[{i}].assign({x}, {y});\n")
            f.write("    double dist_ball_to_point1;\n")
            f.write("    double nearst_ball_to_point1 = ball_pos1.dist(point1[0]);\n")
            f.write("    int number = 1;\n")
            f.write(f"    for(int i = 0; i < {len(point_lines)}; ++i)\n")
            f.write("    {\n")
            f.write("        dist_ball_to_point1 = ball_pos1.dist(point1[i]);\n")
            f.write("        if(dist_ball_to_point1 < nearst_ball_to_point1)\n")
            f.write("        {\n")
            f.write("            nearst_ball_to_point1 = dist_ball_to_point1;\n")
            f.write("            number = i + 1;\n")
            f.write("        }\n")
            f.write("    }\n")
            f.write("    return number;\n")
            f.write("}\n")

    def generate_positions_cpp(self, samples, out_file):
        with open(out_file, 'a') as f:
            f.write("\nrcsc::Vector2D Bhv_BasicMove::Alp_normal_position(const rcsc::WorldModel& wm, int unum)\n{\n")
            f.write("    double point1 = Alp_ground_points(wm);\n")
            f.write("    rcsc::Vector2D pos1[12];\n\n")
            for idx, sample in enumerate(samples):
                f.write(f"    if(point1 == {idx+1})\n")
                f.write("    {\n")
                for unum in sorted(sample["players"].keys()):
                    if 1 <= unum <= 11:
                        x, y = sample["players"][unum]
                        f.write(f"        pos1[{unum}].assign({x}, {y});\n")
                f.write("    }\n\n")
            f.write("    return pos1[unum];\n")
            f.write("}\n")

    def resize_window(self, size_str):
        self.root.geometry(size_str)

    def change_background(self, color):
        self.root.configure(bg=color)
        self.label.configure(bg=color)
        self.status_label.configure(bg=color)

    def show_help(self):
        messagebox.showinfo(
            "Help",
            "You can select a .conf file and generate C++ code.\n"
            "Use the menu options or buttons.\n"
            "Alpha Team Support: emadshojaee.sh@gmail.com"
        )

    def show_about_info(self):
        messagebox.showinfo(
            "About Alpha Conf",
            "Alpha Simulation 2D _ Conf \n"
            "Version: 1.0.0\n"
            "Created by: Alpha Team\n"
            "Contact: emadshojaee.sh@gmail.com"
        )


if __name__ == "__main__":
    root = Tk()
    app = ConfToCppApp(root)
    root.mainloop()
