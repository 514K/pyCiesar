def lb(i,k,a):
    if i == 'а':
        a = a[:k]+a[k].replace('а','ф')+a[k+1:]        
    elif i == 'б':
        a = a[:k]+a[k].replace('б','х')+a[k+1:]        
    elif i == 'в':
        a = a[:k]+a[k].replace('в','ц')+a[k+1:]       
    elif i == 'г':
        a = a[:k]+a[k].replace('г','ч')+a[k+1:]        
    elif i == 'д':
        a = a[:k]+a[k].replace('д','ш')+a[k+1:]      
    elif i == 'е':
        a = a[:k]+a[k].replace('е','щ')+a[k+1:]        
    elif i == 'ё':
        a = a[:k]+a[k].replace('ё','ъ')+a[k+1:]        
    elif i == 'ж':
        a = a[:k]+a[k].replace('ж','ы')+a[k+1:]       
    elif i == 'з':
        a = a[:k]+a[k].replace('з','ь')+a[k+1:]        
    elif i == 'и':
        a = a[:k]+a[k].replace('и','э')+a[k+1:]      
    elif i == 'й':
        a = a[:k]+a[k].replace('й','ю')+a[k+1:]        
    elif i == 'к':
        a = a[:k]+a[k].replace('к','я')+a[k+1:]        
    elif i == 'л':
        a = a[:k]+a[k].replace('л','а')+a[k+1:]       
    elif i == 'м':
        a = a[:k]+a[k].replace('м','б')+a[k+1:]       
    elif i == 'н':
        a = a[:k]+a[k].replace('н','в')+a[k+1:]      
    elif i == 'о':
        a = a[:k]+a[k].replace('о','г')+a[k+1:]     
    elif i == 'п':
        a = a[:k]+a[k].replace('п','д')+a[k+1:]        
    elif i == 'р':
        a = a[:k]+a[k].replace('р','е')+a[k+1:]      
    elif i == 'с':
        a = a[:k]+a[k].replace('с','ё')+a[k+1:]      
    elif i == 'т':
        a = a[:k]+a[k].replace('т','ж')+a[k+1:]     
    elif i == 'у':
        a = a[:k]+a[k].replace('у','з')+a[k+1:]      
    elif i == 'ф':
        a = a[:k]+a[k].replace('ф','и')+a[k+1:]       
    elif i == 'х':
        a = a[:k]+a[k].replace('х','й')+a[k+1:]        
    elif i == 'ц':
        a = a[:k]+a[k].replace('ц','к')+a[k+1:]    
    elif i == 'ч':
        a = a[:k]+a[k].replace('ч','л')+a[k+1:]     
    elif i == 'ш':
        a = a[:k]+a[k].replace('ш','м')+a[k+1:]     
    elif i == 'щ':
        a = a[:k]+a[k].replace('щ','н')+a[k+1:]   
    elif i == 'Ъ':
        a = a[:k]+a[k].replace('ъ','о')+a[k+1:]
    elif i == 'ы':
        a = a[:k]+a[k].replace('ы','п')+a[k+1:]   
    elif i == 'ь':
        a = a[:k]+a[k].replace('ь','р')+a[k+1:]      
    elif i == 'э':
        a = a[:k]+a[k].replace('э','с')+a[k+1:]     
    elif i == 'ю':
        a = a[:k]+a[k].replace('ю','т')+a[k+1:]
    elif i == 'я':
        a = a[:k]+a[k].replace('я','у')+a[k+1:]
    return a