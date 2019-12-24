# import random
#
# enemy_types = ["../images/enemy1.png",
#                "../images/enemy2.png",
#                "../images.enemy3.png"]
# enemy_type = enemy_types[random.randint(0, 2)]
# print(enemy_type)

# a = {"abc": 123}
#
# for i in a:
#     x = a[i]
#     print(x)


# import re
# enemy_types = ["../images/enemy1.png",
#                "../images/enemy2.png",
#                "../images/enemy3_n1.png"]
#
# for enemy_type in enemy_types:
# #     enemy_num = re.match(r".*?/enemy(\d).*?", enemy_type).group(1)
# #     print(enemy_num)
# #     print(type(enemy_num))
#
#     enemy_num = re.search(r"enemy(\d)", enemy_type).group(1)
#     print(enemy_num)
#     print(type(enemy_num))


# boom_image_list0 = []
# boom_image_length0 = 0
# boom_image_list1 = [1]
# boom_image_length1 = 1
# boom_image_list2 = [1, 2]
# boom_image_length2 = 2
# x = [(boom_image_list0, boom_image_length0),
#      (boom_image_list1, boom_image_length1),
#      (boom_image_list2, boom_image_length2)]
#
# a = x[0][1]
# print(a)


# a = {'a': 23}
# for b in a:
#     c = a[b]
#     print(c)
#     print(a['a'])

#
# group0 = [1, 2]
# group1 = [3, 4]
# group2 = [5, 6]
# group3 = [group0, group1, group2]
# for m in group3:
#     x = m.copy()
#     for n in m:
#         if n == 5:
#             x.remove(n)
#
#     print(x)
#     print(m)

# list = [1, 2, 3]
# list.remove(1)
# list.remove(1)
# print(list)


d = dict()
dd1 = d.fromkeys('abc', 123)
dd = d.fromkeys([1, 2, 3], 123)
print(dd1)
print(dd)