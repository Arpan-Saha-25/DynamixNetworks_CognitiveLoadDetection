## 🧠 Cognitive Load Detection from Typing Patterns

### 📌 Overview
This project implements a **privacy-preserving machine learning system** that predicts a user's cognitive load  
(**Low / Medium / High**) using **keystroke timing dynamics** ⌨️.  
The system relies purely on behavioral signals and **does not store or analyze any typed text** 🔐.

This project was developed as part of a **Machine Learning Internship**.

---

### 🎯 Objective
To detect cognitive load using keystroke dynamics such as typing speed, pauses, and timing variability,  
while ensuring **complete user privacy**.

---

### 🧩 Features Used
- ⏱️ **Hold Time** – duration a key is pressed  
- 🔁 **Inter-Key Delay** – time gap between successive keystrokes  
- ⏸️ **Pause Frequency & Duration** – long typing gaps indicating hesitation  
- ⚡ **Typing Speed** – keystrokes per second  

---

### ⚙️ Methodology
1. ⌨️ Capture key press and release timestamps in real time  
2. 📊 Convert raw keystroke events into session-level statistical features  
3. 🏷️ Label sessions as *Low*, *Medium*, or *High* cognitive load using controlled typing tasks  
4. 🌲 Train a **Random Forest Classifier** on the extracted features  
5. 🖥️ Perform real-time prediction using a **30-second typing window**

---

### 📂 Dataset
- Session-based dataset created from multiple typing sessions  
- Each session contains aggregated behavioral features  
- Dataset size is limited; **some samples were augmented for demonstration purposes**

---

### 🤖 Model
- **Algorithm:** Random Forest Classifier  
- **Reason:** Robust to noisy behavioral data and effective with small datasets  

---

### 📈 Results
- ✅ Accuracy: **~75%** on a small test set  
- 🔑 Most influential features:
  - Typing speed  
  - Pause frequency  
  - Inter-key delay variability  

⚠️ Due to limited data, performance may vary. Accuracy is expected to improve with larger real-world datasets.

---

### ▶️ Real-Time Demo
A **terminal-based demo** captures keystrokes for **30 seconds**, extracts features, and predicts cognitive load
in real time.

```bash
python src/realtime_predict.py
```

### 🔐 Privacy Considerations

- ❌ No characters or text content are stored

- ✅ Only timing-based keystroke features are recorded

- 🔒 The system is fully privacy-preserving by design

#### 🛠️ Technologies Used

- 🐍 Python

- 📦 scikit-learn

- 📊 pandas, numpy

- ⌨️ pynput