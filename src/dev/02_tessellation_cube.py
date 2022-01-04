'''
This is a file explaining about tessellation with cube.
'''

# import compas module
from compas.geometry import Point, Polygon, Rotation, Vector, Translation, Box
from compas_view2.app import App
import math as m

# define array length for each dimension
edge_length = 1
arr1d_length = 3
arr2d_length = 3
arr3d_length = 3
view = True

# create original polygon
polygon = Polygon.from_sides_and_radius_xy(4, (edge_length*m.sqrt(2))/2)
R = Rotation.from_axis_and_angle(Vector(0, 0, 1), m.radians(45))
polygon.transform(R)
centroid = polygon.centroid

# 1d array with polygons
polygons_arr1d = []
for i in range(arr1d_length):
    center = Point(i, 0, 0)
    vec = center - centroid
    T = Translation.from_vector(vec)
    polygon_transformed = polygon.transformed(T)
    polygons_arr1d.append(polygon_transformed)

# # 2d array with polygons
polygon_arr2d = []
for i in range(arr1d_length):
    arr1d_temp = []
    for j in range(arr2d_length):
        center = Point(i, j, 0)
        vec = center - centroid
        T = Translation.from_vector(vec)
        polygon_transformed = polygon.transformed(T)
        arr1d_temp.append(polygon_transformed)
    polygon_arr2d.append(arr1d_temp)

# 3d array with box
box = Box.from_width_height_depth(edge_length, edge_length, edge_length)
box_arr3d = []
for i in range(arr3d_length):
    arr2d_temp = []
    for j in range(arr2d_length):
        arr1d_temp = []
        for k in range(arr1d_length):
            center = Point(i*edge_length, j*edge_length, k*edge_length)
            vec = center - centroid
            T = Translation.from_vector(vec)
            box_transformed = box.transformed(T)
            arr1d_temp.append(box_transformed)
        arr2d_temp.append(arr1d_temp)
    box_arr3d.append(arr2d_temp)

# # visualize with compas view2
if view:
    viewer = App()
    # [viewer.add(i) for i in polygons_arr1d]
    # [[viewer.add(j) for j in i] for i in polygon_arr2d]
    [[[viewer.add(k) for k in j] for j in i] for i in box_arr3d]
    viewer.run()
