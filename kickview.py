from tkinter import *
from tkinter import filedialog
from selenium.webdriver.chrome import service
from selenium import webdriver

class TarsKickViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Tars Online Kick Viewer")
        self.root.geometry("420x380")

        self.link = StringVar()
        self.num_tabs = IntVar()
        self.is_muted = BooleanVar()

        self.create_ui()

    def create_ui(self):
        Label(self.root, text="Tars Online Kick Viewer", font=("Helvetica", 20)).pack(pady=20)

        Label(self.root, text="Link to Stream:").pack()
        Entry(self.root, textvariable=self.link).pack()

        Label(self.root, text="Number of tabs to open:").pack()
        Entry(self.root, textvariable=self.num_tabs).pack()

        Checkbutton(self.root, text="Mute tabs", variable=self.is_muted).pack()

        Button(self.root, text="Open Tabs", command=self.open_tabs).pack(pady=20)

    def open_tabs(self):
        chrome_exe_path = filedialog.askopenfilename(title="Select Chrome executable", filetypes=[("Executable files", "*.exe")])

        # Create and configure ChromeDriver options
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = chrome_exe_path

        # Create ChromeDriver service
        chrome_driver_exe_path = r"C:\Users\Sewer\Desktop\val checker\chromedriver.exe"
        webdriver_service = service.Service(chrome_driver_exe_path)

        # Start ChromeDriver service
        webdriver_service.start()

        # Create a list to store remote WebDriver instances
        remote_instances = []

        for _ in range(self.num_tabs.get()):
            # Create remote webdriver using the service URL
            remote = webdriver.Remote(webdriver_service.service_url, options=chrome_options)
            remote.get(self.link.get())
            if self.is_muted.get():
                remote.execute_script("document.querySelector('video').muted = true")
            remote_instances.append(remote)

root = Tk()
app = TarsKickViewer(root)
root.mainloop()
