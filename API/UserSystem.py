def SignUp():
	print("=" * 50)
	print("hi\n由于本人技术有限，所以我们的用户系统采用变量存储，，后续有机会更新自动登录系统（？）")
	print("=" * 50)
	print("该过程存入信息将用于该文件所有涉及信息处理，请勿输入错误信息")
	print("=" * 50)
	UserName = input("请问您的名字？")
	while 1:
		if len(UserName) < 1:
			print("名字不能为空，请重新输入！")
			UserName = input("请重新输入您希望显示的名字：")
		else:
			break
	UserID = input("请输入您的QQ号")
	while 1:
		if len(UserID) < 5:
			print("QQ号必须是5位以上数字，请重新输入！")
			UserID = input(" 请重新输入您的QQ号：")
		elif not UserID.isdigit():
			print("QQ号必须为纯数字，请重新输入！")
			UserID = input(" 请重新输入您的QQ号：")
		else:
			break
	print("=" * 50)
	print("用户信息核对")
	print()
	print(f"名字：{UserName}")
	print(f"ID：{UserID}")
	print()
	print("信息己存入栈")
	print("=" * 50)
SignUp()