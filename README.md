# 🔲 Rectangle & Square (Python OOP)

This project implements two classes — **Rectangle** and **Square** — to practice **object-oriented programming in Python**.  
It includes functionality for calculating dimensions, drawing ASCII-art shapes, and determining how many times one shape can fit inside another.  

---

## ✨ Features

### Rectangle
- Set **width** and **height**
- Calculate:
  - 📐 **Area**  
  - ➖ **Perimeter**  
  - 📏 **Diagonal**  
- Render ASCII **picture** (limited to 50×50 to avoid huge outputs)
- Check how many times another shape fits inside
- Human-readable string representation:
```python
Rectangle(width=16, height=8)
```

### Square
- Inherits from `Rectangle`
- Uses a single **side** instead of width & height
- Keeps width and height always equal
- Human-readable string representation:
```python
Square(side=5)
```

---

## 📖 Example Usage

```python
rect = Rectangle(16, 8)
rect2 = Rectangle(4, 4)

print(rect.get_area())         # 128
print(rect.get_perimeter())    # 48
print(rect.get_diagonal())     # 17.888...
print(rect.get_amount_inside(rect2))  # 8

print(rect.get_picture())
# ****************
# ****************
# ****************
# ****************
# ****************
# ****************
# ****************
# ****************

sq = Square(4)
sq.set_side(5)

print(sq.get_area())      # 25
print(sq.get_picture())
# *****
# *****
# *****
# *****
# *****

print(sq)                 # Square(side=5)
