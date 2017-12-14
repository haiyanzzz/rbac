#!usr/bin/env python
# -*- coding:utf-8 -*-
menu_dict = {
	1: {'id': 1, 'title': '用户列表', 'url': '/userinfo/', 'menu_gp_id': None, 'menu_id': 2, 'menu_title': '菜单二', 'active': True},
	5: {'id': 5, 'title': '订单列表', 'url': '/order/', 'menu_gp_id': None, 'menu_id': 1, 'menu_title': '菜单一'}
}
result = {}
active = False
for item in menu_dict.values():
    result["menu_id"] = {
        "menu_id":item["menu_id"],
        "title":item["title"],
        "active":active,
        "children":[
            {'url': item["url"], 'active': True}
        ]
    }
print(result)
# {
# 	1:{
# 		menu_id:1
# 		menu_title:
# 		active:True
# 		children:[
# 			{'title': '用户列表', 'url': '/userinfo/', 'menu_gp_id': None}
# 		]
# 	  }
# 	 2:{
# 		menu_id:1
# 		menu_title:
# 		active:True
# 		children:[
# 			{'title': '用户列表', 'url': '/userinfo/', 'menu_gp_id': None}
# 		]
# 	  }
# }