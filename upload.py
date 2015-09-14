import xlrd

def addProduct(pro):
	from app.models import products
	product= products(name=pro[2],brand=pro[1],price=pro[4],category=pro[3],description=pro[5],image=pro[0])
	product.save()
	print "added ",pro[2],pro[1],pro[3]
	return


def upload():
	
	sheet= xlrd.open_workbook("miip.xlsx")
	elctronics= sheet.sheet_by_name("electronics")
	food= sheet.sheet_by_name("food")
	fashion= sheet.sheet_by_name("fashion")
	travel= sheet.sheet_by_name("travel")

	for i in range(1,food.nrows):
		p=food.row_values(i)
		print i
		addProduct(p)

	'''
	for i in range(8,21):
		p=elctronics.row_values(i)
		print i
		addProduct(p)

	for i in range(1,fashion.nrows):
		p=fashion.row_values(i)
		addProduct(p[0],p[1],p[2],p[3],[4],p[5])
	
	for i in range(1,travel.nrows):
		p=travel.row_values(i)
		addProduct(p[0],p[1],p[2],p[3],[4],p[5])
	'''
