#Celem jest przedstawienie wielomianu jako funkcję liniową początkową, gdzie znajduje się współczynnik przy x^n oraz
# współczynnik przy x^n-1, która następnie jest mnożona razy x oraz dodaje się do niej
#kolejny współczynnik przy kolejnej potędze x co daje nam kolejny wyraz do pomnnożenia razy x. Takich operacji mnożenia
#wykonujemy n, (ponieważ x do potęgi n-tej musimu uzyskać) oraz n dodawań kolejnych współczynników przy x do niższej
# potegi a to daje nam O(n) + O(n) = 2*O(n) = O(n)
#                                           -------