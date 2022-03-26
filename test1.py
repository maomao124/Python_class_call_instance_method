"""
 * Project name(项目名称)：Python类调用实例方法
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/26 
 * Time(创建时间)： 21:18
 * Version(版本): 1.0
 * Description(描述)： Python 中允许使用类名直接调用实例方法，但必须手动为该方法的第一个 self 参数传递参数，这种调用方法的方式被称为“非绑定方法”。
 用类的实例对象访问类成员的方式称为绑定方法，而用类名调用类成员的方式称为非绑定方法。
 """


class C:
    def f1(self):
        """
        实例方法f1
        :return:
        """
        print("实例方法f1")


if __name__ == '__main__':
    # 通过类名直接调用实例方法,不允许
    # C.f1()
    c = C()
    # 通过类名直接调用实例方法
    C.f1(c)
    c.f1()


