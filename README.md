分解layaair项目打包的图集文件，需要图集数据（atlas）和图集图片（png），分解时会在图集所在目录下创建同名目录，该图集分解出来的图片全部放在该目录中
<br>
<br>需要python环境和Pillow库
<br>
<br>分解当前目录所有atlas（递归）
<br>python splitLayaAtlas.py
<br>
<br>分解指定图集文件
<br>python splitLayaAtlas.py -name [filename]
<br>filename替换为你要分解的图集文件名（不带.atlas）