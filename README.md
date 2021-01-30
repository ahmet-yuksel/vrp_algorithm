# vrp_algorithm

algoritmada önce araçların kombinasyonları hesaplanır.

verilen input dataya göre kombinasyonlar bulunur.

`[1,2,3],[1,2],[1,3],[2,3],[1],[2],[3]`

bu değerlere göre siğarişlerin araçlara dağılım kombinasyonları bulunur.

`{1:[1,2,3,4,5,6,7],2:[],3[]
{1:[1],2:[2,3,4,5,6,7],3[]
{1:[1],2:[],3[2,3,4,5,6,7]
{1:[1],2:[2],3[3,4,5,6,7]` ...


sonrasında sort edilmiş bu listeden mükerrer olanlar silinir. Aşağıda olduğu gibi bu route birbirin aynısıdır. Sonraki adımda permütasyon fonksiyonu kullanarak siparişlerin farklı dizilimleri bulunup süreleri hesaplanacak minimum süreye sahip olan buluncaktır.

`{1:[1,2,3,4,5,6,7],2:[],3[]
{1:[7,6,5,4,3,2,1],2:[],3[]`

Elimizde bütün vehcile-order eşleşmeleri bulunmuştur.

Sonraki adımda route ların her biri için min süreler hesaplanır. Süreler hesaplanırken her bir araç için siparişlerin sıralama olasılığı hesaplanır ve minimum süreleri bulunur. Sonrasın da route toplam süresi hesaplanır. 
Bu hesaplama şu şekilde yapılır. Örneğin  
`2 nolu araçın rotası :2:[5,6]   vehicle id 2-> order id 5->order id 6-> vehicle id 2`

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

`#return {1:[2,1],2:[5,6],3:[4,7,3], 'Total_second':4000}`

her bir route için total süre hesaplandığı için küçükten büyüğe göre sıralanır ve sıralanmış rotalar output dosyasına yazdırılır.

##### **Not: Araçların tümünün sipariş dağıtma zorunluğu belirtilmediği için bazı araçlara sipariş atanmama ihtimalleri de hesaplanmış ve değerlendirmeye katılmıştır.**



