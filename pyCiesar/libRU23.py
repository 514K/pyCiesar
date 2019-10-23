def lb(i,k,a):
    if i == 'а':
        a = a[:k]+a[k].replace('а','ц')+a[k+1:]        
    elif i == 'б':
        a = a[:k]+a[k].replace('б','ч')+a[k+1:]        
    elif i == 'в':
        a = a[:k]+a[k].replace('в','ш')+a[k+1:]       
    elif i == 'г':
        a = a[:k]+a[k].replace('г','щ')+a[k+1:]        
    elif i == 'д':
        a = a[:k]+a[k].replace('д','ъ')+a[k+1:]      
    elif i == 'е':
        a = a[:k]+a[k].replace('е','ы')+a[k+1:]        
    elif i == 'ё':
        a = a[:k]+a[k].replace('ё','ь')+a[k+1:]        
    elif i == 'ж':
        a = a[:k]+a[k].replace('ж','э')+a[k+1:]       
    elif i == 'з':
        a = a[:k]+a[k].replace('з','ю')+a[k+1:]        
    elif i == 'и':
        a = a[:k]+a[k].replace('и','я')+a[k+1:]      
    elif i == 'й':
        a = a[:k]+a[k].replace('й','а')+a[k+1:]        
    elif i == 'к':
        a = a[:k]+a[k].replace('к','б')+a[k+1:]        
    elif i == 'л':
        a = a[:k]+a[k].replace('л','в')+a[k+1:]       
    elif i == 'м':
        a = a[:k]+a[k].replace('м','г')+a[k+1:]       
    elif i == 'н':
        a = a[:k]+a[k].replace('н','д')+a[k+1:]      
    elif i == 'о':
        a = a[:k]+a[k].replace('о','е')+a[k+1:]     
    elif i == 'п':
        a = a[:k]+a[k].replace('п','ё')+a[k+1:]        
    elif i == 'р':
        a = a[:k]+a[k].replace('р','ж')+a[k+1:]      
    elif i == 'с':
        a = a[:k]+a[k].replace('с','з')+a[k+1:]      
    elif i == 'т':
        a = a[:k]+a[k].replace('т','и')+a[k+1:]     
    elif i == 'у':
        a = a[:k]+a[k].replace('у','й')+a[k+1:]      
    elif i == 'ф':
        a = a[:k]+a[k].replace('ф','к')+a[k+1:]       
    elif i == 'х':
        a = a[:k]+a[k].replace('х','л')+a[k+1:]        
    elif i == 'ц':
        a = a[:k]+a[k].replace('ц','м')+a[k+1:]    
    elif i == 'ч':
        a = a[:k]+a[k].replace('ч','н')+a[k+1:]     
    elif i == 'ш':
        a = a[:k]+a[k].replace('ш','о')+a[k+1:]     
    elif i == 'щ':
        a = a[:k]+a[k].replace('щ','п')+a[k+1:]   
    elif i == 'Ъ':
        a = a[:k]+a[k].replace('ъ','р')+a[k+1:]
    elif i == 'ы':
        a = a[:k]+a[k].replace('ы','с')+a[k+1:]   
    elif i == 'ь':
        a = a[:k]+a[k].replace('ь','т')+a[k+1:]      
    elif i == 'э':
        a = a[:k]+a[k].replace('э','у')+a[k+1:]     
    elif i == 'ю':
        a = a[:k]+a[k].replace('ю','ф')+a[k+1:]
    elif i == 'я':
        a = a[:k]+a[k].replace('я','х')+a[k+1:]
    return a