## Cognitive Load Detection from Typing Patterns

### Objective
Predict cognitive load (Low/Medium/High) using keystroke timing dynamics without storing text.

### Features
- Hold time
- Inter-key delay
- Pause frequency & duration
- Typing speed

### Model
Random Forest Classifier

### Results
- Accuracy: ~75% (limited data)
- Key features: typing speed, pauses, inter-key delay

### Real-Time Demo
Terminal-based prediction using 30-second typing session.

### Privacy
No text or characters are stored at any point.
