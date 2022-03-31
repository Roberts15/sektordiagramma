import matplotlib.pyplot as plt
maize=[27, 70, 258, 78, 8]
veidi=["Sēklu maize", "Rupjmaize", "Baltmaize", "Ķieģelīši", "Ķimeņu maize"]
krasa=["red","gray","#E9967A", "#8B4513", "orange"]
pppietupies=[0.5, 0, 0, 0, 0]
plt.pie(maize)
plt.pie(maize, labels=veidi, colors=krasa, autopct="%1.1f%%", explode=pppietupies)
plt.show()