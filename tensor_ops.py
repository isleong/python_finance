#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  tensor_ops.py
#  
#  Copyright 2017 I-Shen Leung <i-shenl@ishenl-HP-EliteBook-850-G1>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


from __future__ import print_function

import tensorflow as tf

a = tf.constant(2)
b = tf.constant(3)

with tf.Session() as sess:
	print("a=2 b=3")
	print("Addition with constants: %i" % sess.run(a+b))
	print("Multiplication with constants: %i" % sess.run(a*b))
	
a = tf.placeholder(tf.int16)
b = tf.placeholder(tf.int16)

add = tf.add(a, b)
mul = tf.multiply(a, b)

matrix1 = tf.constant([[3., 3.]])
matrix2 = tf.constant([[2.], [2.]])

product = tf.matmul(matrix1, matrix2)

with tf.Session() as sess:
	result = sess.run(product)
	print(result)

