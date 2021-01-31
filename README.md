# vrp_algorithm
`python 3.7.3` kurulu bilgisayarda veya enviroment'a **herhangi bir lib kurulumu gerekmeden** proje dizinde iken 
`python  main.py` ile program çalıştırılır ekranda aşağı gibi kullanıcıdan input beklenir

`Select optimal route(o) or total seconds(t) :`

`o` seçilirse( **optimal route ** ) :araçların rotasının tamamlama sürelerinin maksimum değerini dikkate alarak oluşturulan routelardır.

`t` seçilirse ( **total seconds ** ) : her bir aracın rotasının tamamlama sürelerinin toplamı dikkate alarak oluşturulan routelardır.

# algoritma akışı 
İlk adımda araçların kombinasyonları hesaplanır. verilen input dataya göre kombinasyonlar bulunur.

`[1,2,3],[1,2],[1,3],[2,3],[1],[2],[3]`

bu değerlere göre siparişlerin araçlara dağılım kombinasyonları bulunur.

`{1:[1,2,3,4,5,6,7],2:[],3[]
{1:[1],2:[2,3,4,5,6,7],3[]
{1:[1],2:[],3[2,3,4,5,6,7]
{1:[1],2:[2],3[3,4,5,6,7]` ...


sonrasında sort edilmiş bu listeden mükerrer olanlar silinir. 

Aşağıdaki routelar birbirinin aynısıdır. Sonraki adımda order sıraları permütasyon fonksiyonu kullanarak  bulunacak ve süreleri hesaplanacaktır.

`{1:[1,2,3,4,5,6,7],2:[],3[]
{1:[7,6,5,4,3,2,1],2:[],3[]`

Tüm vehcile-order eşleşmelerinin listesi bulunmuştur .

Sonraki adımda route ların her biri için min süreler hesaplanır. Süreler hesaplanırken her bir araç için siparişlerin sıralama olasılığı hesaplanır ve minimum süreleri bulunur. Sonrasın da route toplam süresi ve optimal route değeri hesaplanır. 
Bu hesaplama şu şekilde yapılır. Örneğin  
`2 nolu araç için rota 2:[5,6]`

gezinme rotası :`vehicle id 2-> order id 5->order id 6-> vehicle id 2`

bir rotanın hesalanma yöntemi
`#route :{1:[1,2],2:[5,6],3:[3,4,7]}`

`# 1:[1,2] = 3000 sec`

`# 1:[2,1] = 2000 sec *`

`# 2:[5,6] = 1000 sec *`

`# 2:[6,5] = 2500 sec`

`# 3:[3,4,7] = 1300 sec`

`# 3:[4,3,7] = 1200 sec`

`# 3:[7,3,4] = 1900 sec`

`# 3:[4,7,3] = 1000 sec *`

`# 3:[3,7,4] = 1700 sec`

`# 3:[7,4,3] = 4000 sec`

`#return {1:[2,1],2:[5,6],3:[4,7,3], 'total_second':4000 'optimal_second':2000}:`

kullanıcının optimal route ve total seconds seçimine göre 

her bir route için  hesaplanan optimal route değeri küçükten büyüğe göre sıralanır veya
her bir route hesaplanan total seconds için küçükten büyüğe göre sıralanır 


ve sıralanmış rotalar output dosyasına yazdırılır.

##### **Not 1: Araçların tümünün sipariş dağıtma zorunluğu belirtilmediği için bazı araçlara sipariş atanmama ihtimalleri de seçenek olarak sunulmuştur.**
##### **Not 2: Optimal route için route daki araçların dağıtım sürelerin maksimum değeri optimal değer olarak hesaplanır. Bu değer araçlar aynı anda dağıtıma başlarsa tüm siparişlerin ne kadar sürede dağılacağını da gösterir. Kullanıcı isterse bu değere sonuçları alabilmesi için seçenek olarak sunulmuştur  **
##### **Not 3: Ortools kullanarak bulunan optimal route rotası, bu algoritma optimal route seçeneği seçilerek elde edilen sonuçta ikinci sıra da yer almaktadır. Daha düşük bir optimal route değeri sahip route ilk sırada yer almmaktadır.**


