from sklearn import tree
clf = tree.DecisionTreeClassifier()
## Boy , Kilo , Yaş
DataSet = [[165, 66, 16], [163, 98, 15], [148, 34, 17], [173, 54, 18], [191, 70, 16],[190, 90, 17], [175, 64, 28],
[182, 45, 28], [164, 87, 17], [142, 68, 16], [176, 57, 21]]
Gender = ["homina", "homina", "domina", "domina", "homina", "homina", "domina", "domina",
"domina", "homina", "homina"]
clf = clf.fit(DataSet, Gender)
prediction = clf.predict([[180, 55, 18]])
print(prediction)