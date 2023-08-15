import tkinter as tk
import nmap
import os
import subprocess


class NetworkScannerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Network Scanner App")

        self.detect_devices_button = tk.Button(root, text="Detect Devices", command=self.detect_devices)
        self.detect_devices_button.pack(padx=10, pady=10)

    def detect_devices(self):
        nm = nmap.PortScanner()
        nm.scan(hosts="192.168.1.0/24", arguments="-sn")

        self.device_list_window = tk.Toplevel(self.root)
        self.device_list_window.title("Detected Devices")

        self.device_list = tk.Listbox(self.device_list_window)
        self.device_list.pack(fill="both", expand=True)

        for host in nm.all_hosts():
            self.device_list.insert("end", host)

        self.actions_frame = tk.Frame(self.device_list_window)
        self.actions_frame.pack(padx=10, pady=10)

        scan_ports_button = tk.Button(self.actions_frame, text="Scan Ports", command=self.scan_ports)
        scan_ports_button.pack(side="left", padx=10)

        view_details_button = tk.Button(self.actions_frame, text="View Details", command=self.view_details)
        view_details_button.pack(side="left", padx=10)

        ping_button = tk.Button(self.actions_frame, text="Ping", command=self.ping)
        ping_button.pack(side="left", padx=10)

        traceroute_button = tk.Button(self.actions_frame, text="Traceroute", command=self.traceroute)
        traceroute_button.pack(side="left", padx=10)

    def scan_ports(self):
        selected_item = self.device_list.get(tk.ACTIVE)

        nm = nmap.PortScanner()
        nm.scan(hosts=selected_item, arguments="-p1-1024 -T4")
        open_ports = [port for port in nm[selected_item]["tcp"] if nm[selected_item]["tcp"][port]["state"] == "open"]

        open_ports_text = ", ".join(map(str, open_ports))  # Convertir los números enteros a cadenas
        result_text = f"Open ports on {selected_item}: {open_ports_text}"

        self.show_result("Port Scan Result", result_text)

    def view_details(self):
        selected_item = self.device_list.get(tk.ACTIVE)

        nm = nmap.PortScanner()
        nm.scan(hosts=selected_item, arguments="-O -T4")

        os_details = nm[selected_item].get("osmatch", [])
        if os_details:
            os_name = os_details[0].get("name", "Unknown OS")
            os_accuracy = os_details[0].get("accuracy", "N/A")
        else:
            os_name = "Unknown OS"
            os_accuracy = "N/A"

        details_text = f"IP Address: {selected_item}\n"
        details_text += f"Hostname: {nm[selected_item].hostname()}\n"
        details_text += f"OS Name: {os_name}\n"
        details_text += f"OS Accuracy: {os_accuracy}\n"

        self.show_result("Device Details", details_text)

    def ping(self):
        selected_item = self.device_list.get(tk.ACTIVE)

        response = os.system(f"ping {selected_item}")
        if response == 0:
            ping_result = f"{selected_item} is up"
        else:
            ping_result = f"{selected_item} is down"

        self.show_result("Ping Result", ping_result)

    def traceroute(self):
        selected_item = self.device_list.get(tk.ACTIVE)

        try:
            traceroute_output = subprocess.check_output(["traceroute", selected_item], stderr=subprocess.STDOUT,
                                                        text=True)
            self.show_result("Traceroute Result", traceroute_output)
        except subprocess.CalledProcessError as e:
            self.show_result("Traceroute Result", e.output)

    def show_result(self, title, result_text):
        result_window = tk.Toplevel(self.root)
        result_window.title(title)

        result_label = tk.Label(result_window, text=result_text)
        result_label.pack(padx=10, pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = NetworkScannerApp(root)
    root.mainloop()