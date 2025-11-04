import os
import shutil

# 👇 Change these paths to your actual label folders
A_train = "C:\\Users\\edgar\\Desktop\\data\\labels\\Class A\\train"
A_val   = "C:\\Users\\edgar\\Desktop\\data\\labels\\Class A\\val"
B_train = "C:\\Users\\edgar\\Desktop\\data\\labels\\Class B\\train"
B_val   = "C:\\Users\\edgar\\Desktop\\data\\labels\\Class B\\val"


def fix_labels(folder_path):
    """
    Fixes YOLO label files by:
    - Detecting class ID automatically (Class A → 0, Class B → 1)
    - Splitting merged lines into valid YOLO format (1 bbox per line)
    - Creating backups before modifying
    - Counting how many labels were fixed per file
    """

    # 🧭 Detect which class the folder belongs to
    folder_lower = folder_path.lower()
    if "class a" in folder_lower:
        new_class_id = 0
    elif "class b" in folder_lower:
        new_class_id = 1
    else:
        print(f"⚠ Skipped {folder_path} (class not recognized)")
        return

    print(f"\n🔧 Fixing labels in: {folder_path} → class {new_class_id}")

    # 📁 Create backup folder beside the label folder
    backup_folder = os.path.join(folder_path, "_backup")
    os.makedirs(backup_folder, exist_ok=True)

    total_fixed = 0

    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            backup_path = os.path.join(backup_folder, filename)

            # 🧾 Backup original file
            shutil.copy2(file_path, backup_path)

            with open(file_path, "r") as f:
                content = f.read().strip().split()

            fixed_lines = []

            # YOLO format = [class_id, x_center, y_center, width, height]
            for i in range(0, len(content), 5):
                group = content[i:i+5]
                if len(group) == 5:
                    group[0] = str(new_class_id)
                    fixed_lines.append(" ".join(group) + "\n")

            # ✏️ Write corrected lines back to file
            with open(file_path, "w") as f:
                f.writelines(fixed_lines)

            print(f"  ✔ {filename}: {len(fixed_lines)} labels fixed")
            total_fixed += len(fixed_lines)

    print(f"✅ Done fixing: {folder_path}")
    print(f"🗂 Backup saved to: {backup_folder}")
    print(f"📊 Total labels fixed in folder: {total_fixed}\n")


# 👇 Run for all your folders
for folder in [A_train, A_val, B_train, B_val]:
    fix_labels(folder)

print("🎉 All labels fixed successfully (with backups and counts)!")
