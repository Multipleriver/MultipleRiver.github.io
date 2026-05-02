import numpy as np
import matplotlib.pyplot as plt

# 1. 全局字体与样式设置
# 设置所有文本为 Times New Roman 字体
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.rcParams['mathtext.fontset'] = 'custom'
plt.rcParams['mathtext.rm'] = 'Times New Roman'
plt.rcParams['mathtext.it'] = 'Times New Roman:italic'
plt.rcParams['axes.unicode_minus'] = False 

# 2. 创建 4K 分辨率画布 (16:9比例, 3840x2160)
# dpi=240, figsize=(16, 9) 意味着输出分辨率为 3840 x 2160
fig, ax = plt.subplots(figsize=(16, 9), dpi=240, facecolor='white')
ax.set_facecolor('white')

# 3. 数据生成
t = np.linspace(-1.2, 1.2, 5000)

# 理想方波
square_wave = np.where(t > 0, 1.0, -1.0)
square_wave[t == 0] = 0.0

# 傅里叶部分和函数
def fourier_series(t, N):
    y = np.zeros_like(t)
    for k in range(N + 1):
        n = 2 * k + 1
        y += (1 / n) * np.sin(n * np.pi * t)
    return (4 / np.pi) * y

s3 = fourier_series(t, 3)
s10 = fourier_series(t, 10)
s50 = fourier_series(t, 50)

# 4. 绘制曲线
ax.plot(t, square_wave, label='Square wave', color='#1f77b4', linewidth=2.5)
ax.plot(t, s3, label='$S_3(t)$', color='#ff7f0e', linewidth=2)
ax.plot(t, s10, label='$S_{10}(t)$', color='#2ca02c', linewidth=2)
ax.plot(t, s50, label='$S_{50}(t)$', color='#d62728', linewidth=2)

# 5. 图表修饰
ax.set_title('Gibbs Phenomenon Near a Jump Discontinuity', fontsize=26, pad=20)
ax.set_xlabel('Time (t)', fontsize=22)
ax.set_ylabel('Amplitude', fontsize=22)
ax.tick_params(axis='both', which='major', labelsize=18)

# 网格线与参考线
ax.grid(True, linestyle='--', alpha=0.5)
ax.axhline(y=1, color='gray', linestyle=':', alpha=0.8)
ax.axhline(y=-1, color='gray', linestyle=':', alpha=0.8)
ax.axvline(x=0, color='gray', linestyle=':', alpha=0.8)

# 6. 添加 Gibbs 现象的红色箭头标注
# 找到 S50 在 t>0 侧的第一个极值点 (过冲点)
peak_t = 1.0 / (2 * 51)
peak_y = fourier_series(np.array([peak_t]), 50)[0]

ax.annotate('Gibbs Phenomenon', 
            xy=(peak_t, -1.15), 
            xytext=(0.25, -1.35),
            arrowprops=dict(facecolor='#d62728', edgecolor='#d62728', shrink=0.05, width=3, headwidth=10),
            fontsize=22, 
            color='#d62728',
            fontweight='bold')

# 图例设置
ax.legend(fontsize=20, loc='center right', framealpha=1.0, edgecolor='black')

# 设置坐标轴范围
ax.set_xlim([-1.2, 1.2])
ax.set_ylim([-1.5, 1.5])

# 7. 紧凑布局并保存为纯白底色的 4K 图片
plt.tight_layout()
plt.savefig('gibbs_phenomenon_4k.png', dpi=240, bbox_inches='tight', facecolor='white', transparent=False)
print("4K图片 'gibbs_phenomenon_4k.png' 已成功生成并保存！")