#broilerplate code
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.gridspec as gridspec
x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [25, 16, 9, 4, 1]
plt.plot(x, y1, label='Quadratic')

#1
plt.legend(loc='lower left')
plt.show()

#2
plt.legend(loc='upper left', fontsize=16)

#3
plt.legend(loc='upper left', handletextpad=2)

#4
plt.plot(x, y1, label='Quadratic')
plt.plot(x, y2, label='Inverse Quadratic')
plt.legend(ncol=2)  # Use 2 columns
plt.show()

#5
fig, axs = plt.subplots(1, 2)
axs[0].plot([1, 2, 3], [4, 5, 6], label='Line 1')
axs[1].plot([1, 2, 3], [6, 5, 4], label='Line 2')
fig.legend(loc='upper center', ncol=2)
plt.show()

#6
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [4, 5, 6], label='Line 1')
ax.plot([1, 2, 3], [6, 5, 4], label='Line 2')
legend_handles = [
    patches.Patch(color='blue', label='Blue Box'),
    patches.Patch(color='red', label='Red Box')
]
plt.legend(handles=legend_handles, loc='upper right')

plt.show()

#7
fig, axs = plt.subplots(1, 2)
axs[0].plot([1, 2, 3], [4, 5, 6])
axs[0].set_title('Subplot 1')
axs[1].plot([1, 2, 3], [6, 5, 4])
axs[1].set_title('Subplot 2')
plt.show()

#8
fig, axs = plt.subplots(1, 2)
axs[0].plot([1, 2, 3], [4, 5, 6])
axs[1].plot([1, 2, 3], [6, 5, 4])
fig.suptitle('Main Title for All Subplots')
plt.show()

#9
fig, axs = plt.subplots(1, 2)
axs[0].plot([1, 2, 3], [4, 5, 6])
axs[1].plot([1, 2, 3], [6, 5, 4])
axs[0].set_axis_off()
axs[1].set_axis_off()
plt.show()

#10
fig = plt.figure()
gs = gridspec.GridSpec(1, 2, width_ratios=[2, 1])
ax1 = plt.subplot(gs[0])  
ax2 = plt.subplot(gs[1])  
ax1.plot([1, 2, 3], [4, 5, 6])
ax2.plot([1, 2, 3], [6, 5, 4])
ax1.set_title('Larger Subplot')
ax2.set_title('Smaller Subplot')
plt.show()

#11
fig, axs = plt.subplots(1, 2)
axs[0].plot([1, 2, 3], [4, 5, 6])
axs[1].plot([1, 2, 3], [6, 5, 4])
fig.subplots_adjust(wspace=0.5, hspace=0.5)
plt.show()

#12
fig, ax = plt.subplots()
ax.axhline(y=2, color='r', linestyle='--')
plt.show()

#13
ax.axvline(x=2, color='b', linestyle='--')

#14
ax.axhline(y=2, color='r', linestyle='--', alpha=0.5)

#15
ax.axhline(y=2, color='r', linestyle='--', linewidth=10)

#16
x = [1, 2, 3, 4, 5]
y1 = [1, 4, 6, 8, 10]
y2 = [2, 3, 5, 7, 9]
fig, ax = plt.subplots()
ax.plot(x, y1, label='Line 1', color='b')
ax.plot(x, y2, label='Line 2', color='r')
ax.fill_between(x, y1, y2, where=(np.array(y1) > np.array(y2)), color='gray', alpha=0.5)
plt.legend()
plt.show()

#17
categories = ['A', 'B', 'C', 'D']
values = [4, 7, 1, 8]
fig, ax = plt.subplots()
ax.barh(categories, values, color='black')
plt.show()

#18
bars = ax.bar(categories, values, color='black')
ax.bar_label(bars, fmt='%d')
plt.show()

#21
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
fig, ax = plt.subplots()
ax.scatter(x, y, color='b', label='Data Points')
ax.legend()
plt.show()

#22
colors = ['red', 'blue', 'green', 'purple']
fig, ax = plt.subplots()
ax.scatter(x, y, c=colors)
plt.show()

#23
sizes = [50, 100, 300, 400]
fig, ax = plt.subplots()
ax.scatter(x, y, s=sizes)
plt.show()

#24
fig, ax = plt.subplots()
ax.scatter(x, y)
ax.plot(x, y)
plt.show()