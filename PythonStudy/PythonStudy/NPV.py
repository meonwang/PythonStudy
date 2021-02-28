def npv(arraySizes):
  npvs = []
  # X * (1.02+1.02^2 .... 1.02^25)
  pvOf25Years = pv(1.02, 25)

  for arraySize in arraySizes:
    # 1. calculate total investment
    panelPrice = 1860.28571428571 * arraySize + 5712.85714285714
    installationFee = 0.25 * panelPrice
    totalInvestment = panelPrice + installationFee + 1837
    
    # 2. calculate the cash inflows
    # HST 13%
    annualSaving = 0
    taxSaving = 0
    credit = 0
    totalSaving = 0
    if 1175 * arraySize >= 7070.6 * 0.95:
      print("True")
      annualSaving = 0.95 * 1.02 * 874.73
    else:
      print("False")
      annualSaving = 1.02 * 874.73 * 1175 * arraySize / (7070.6 * 0.95)
    credit = annualSaving - 18 * 12
    taxSaving = 0.13 * credit
    totalSaving = (taxSaving + credit) * pvOf25Years
    
    # NPV
    npv = totalSaving - totalInvestment
    npvs.append(npv)
    
    debugMessage = "arraySize: {0}\r\npanelPrice: {1}\r\ninstallationFee: {2}\r\ntotalInvestment: {3}\r\ncredit: {4}\r\ntaxSaving: {5}\r\nnpv: {6}\r\n\r\n"
    # print(debugMessage.format(arraySize, panelPrice, installationFee, totalInvestment, credit, taxSaving, npv))
    
  return npvs

def pv(wacc, numberOfYears):
  res = 0
  temp = 1
  for i in range(1, numberOfYears + 1):
    temp /= wacc
    res += temp
    
  return res
      
print(npv([5, 6, 7, 8, 9, 10]))

