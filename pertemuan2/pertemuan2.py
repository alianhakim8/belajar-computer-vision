# import library opencv
import cv2

print("Program dimulai")

# load image
img = cv2.imread('assets/gambar.png', 1)
# print(img.shape)
# print(img[100, 100, 0])
print(img)

# mengatur ukuran window supaya yang tampil gak kebesaran
imS = cv2.resize(img, (960, 540))

# tampilkan dalam 1 window utama
cv2.imshow("green mountain", imS)

# tunggu action dari user
cv2.waitKey(0)

# hapus semua window yang ada
cv2.destroyAllWindows()

print("Program selesai")
