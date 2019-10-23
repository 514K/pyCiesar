def lb(i,k,a):
    if i == 'а':
        a = a[:k]+a[k].replace('а','в')+a[k+1:]        
    elif i == 'б':
        a = a[:k]+a[k].replace('б','г')+a[k+1:]        
    elif i == 'в':
        a = a[:k]+a[k].replace('в','д')+a[k+1:]       
    elif i == 'г':
        a = a[:k]+a[k].replace('г','е')+a[k+1:]        
    elif i == 'д':
        a = a[:k]+a[k].replace('д','ё')+a[k+1:]      
    elif i == 'е':
        a = a[:k]+a[k].replace('е','ж')+a[k+1:]        
    elif i == 'ё':
        a = a[:k]+a[k].replace('ё','з')+a[k+1:]        
    elif i == 'ж':
        a = a[:k]+a[k].replace('ж','и')+a[k+1:]       
    elif i == 'з':
        a = a[:k]+a[k].replace('з','й')+a[k+1:]        
    elif i == 'и':
        a = a[:k]+a[k].replace('и','к')+a[k+1:]      
    elif i == 'й':
        a = a[:k]+a[k].replace('й','л')+a[k+1:]        
    elif i == 'к':
        a = a[:k]+a[k].replace('к','м')+a[k+1:]        
    elif i == 'л':
        a = a[:k]+a[k].replace('л','н')+a[k+1:]       
    elif i == 'м':
        a = a[:k]+a[k].replace('м','о')+a[k+1:]       
    elif i == 'н':
        a = a[:k]+a[k].replace('н','п')+a[k+1:]      
    elif i == 'о':
        a = a[:k]+a[k].replace('о','р')+a[k+1:]     
    elif i == 'п':
        a = a[:k]+a[k].replace('п','с')+a[k+1:]        
    elif i == 'р':
        a = a[:k]+a[k].replace('р','т')+a[k+1:]      
    elif i == 'с':
        a = a[:k]+a[k].replace('с','у')+a[k+1:]      
    elif i == 'т':
        a = a[:k]+a[k].replace('т','ф')+a[k+1:]     
    elif i == 'у':
        a = a[:k]+a[k].replace('у','х')+a[k+1:]      
    elif i == 'ф':
        a = a[:k]+a[k].replace('ф','ц')+a[k+1:]       
    elif i == 'х':
        a = a[:k]+a[k].replace('х','ч')+a[k+1:]        
    elif i == 'ц':
        a = a[:k]+a[k].replace('ц','ш')+a[k+1:]    
    elif i == 'ч':
        a = a[:k]+a[k].replace('ч','щ')+a[k+1:]     
    elif i == 'ш':
        a = a[:k]+a[k].replace('ш','ъ')+a[k+1:]     
    elif i == 'щ':
        a = a[:k]+a[k].replace('щ','ы')+a[k+1:]   
    elif i == 'Ъ':
        a = a[:k]+a[k].replace('ъ','ь')+a[k+1:]
    elif i == 'ы':
        a = a[:k]+a[k].replace('ы','э')+a[k+1:]   
    elif i == 'ь':
        a = a[:k]+a[k].replace('ь','ю')+a[k+1:]      
    elif i == 'э':
        a = a[:k]+a[k].replace('э','я')+a[k+1:]     
    elif i == 'ю':
        a = a[:k]+a[k].replace('ю','а')+a[k+1:]
    elif i == 'я':
        a = a[:k]+a[k].replace('я','б')+a[k+1:]
    return a