from django.contrib import admin
from .models import choice, question
admin.site.register(question)
admin.site.register(choice)

# Register your models here.
/* hàm đổi từ giây thành giờ phút giây */
  public static void change(int n){
    //khai báo 3 biến hour, minute, second đại diện cho giờ phút giây
    int hour, minute, second;
    //1h = 3600s -> hour = n / 3600
    hour = n / 3600;
    //1p = 60s, vì ở trên ta đã chia 3600 để lấy giờ
    //vậy nên ta cần lấy phần dư của nó chia cho 60
    minute = n % 3660 / 60;
    //phần dư còn lại chính là số giây
    second = n % 3600 % 60;
    System.out.printf("Sau khi đổi từ %d giây: %d:%d:%d",n,hour,minute,second);
  }

    // Nhap input tu ban phim
    int input;
    Scanner sc = new Scanner(System.in);
    System.out.print("\nNhập số giây: ");
    input = sc.nextInt();

    int gio, phut, giay;
    gio = input/3600;
    phut = input % 3660 / 60;
    giay = input % 3600 % 60;
    System.out.printf("\nKêt quả la: ",gio," giờ", phut, " phút", giây, " giây"};