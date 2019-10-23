def lb(i,k,a):
    if i == 'а':
        a = a[:k]+a[k].replace('а','д')+a[k+1:]        
    elif i == 'б':
        a = a[:k]+a[k].replace('б','е')+a[k+1:]        
    elif i == 'в':
        a = a[:k]+a[k].replace('в','ё')+a[k+1:]       
    elif i == 'г':
        a = a[:k]+a[k].replace('г','ж')+a[k+1:]        
    elif i == 'д':
        a = a[:k]+a[k].replace('д','з')+a[k+1:]      
    elif i == 'е':
        a = a[:k]+a[k].replace('е','и')+a[k+1:]        
    elif i == 'ё':
        a = a[:k]+a[k].replace('ё','й')+a[k+1:]        
    elif i == 'ж':
        a = a[:k]+a[k].replace('ж','к')+a[k+1:]       
    elif i == 'з':
        a = a[:k]+a[k].replace('з','л')+a[k+1:]        
    elif i == 'и':
        a = a[:k]+a[k].replace('и','м')+a[k+1:]      
    elif i == 'й':
        a = a[:k]+a[k].replace('й','н')+a[k+1:]        
    elif i == 'к':
        a = a[:k]+a[k].replace('к','о')+a[k+1:]        
    elif i == 'л':
        a = a[:k]+a[k].replace('л','п')+a[k+1:]       
    elif i == 'м':
        a = a[:k]+a[k].replace('м','р')+a[k+1:]       
    elif i == 'н':
        a = a[:k]+a[k].replace('н','с')+a[k+1:]      
    elif i == 'о':
        a = a[:k]+a[k].replace('о','т')+a[k+1:]     
    elif i == 'п':
        a = a[:k]+a[k].replace('п','у')+a[k+1:]        
    elif i == 'р':
        a = a[:k]+a[k].replace('р','ф')+a[k+1:]      
    elif i == 'с':
        a = a[:k]+a[k].replace('с','х')+a[k+1:]      
    elif i == 'т':
        a = a[:k]+a[k].replace('т','ц')+a[k+1:]     
    elif i == 'у':
        a = a[:k]+a[k].replace('у','ч')+a[k+1:]      
    elif i == 'ф':
        a = a[:k]+a[k].replace('ф','ш')+a[k+1:]       
    elif i == 'х':
        a = a[:k]+a[k].replace('х','щ')+a[k+1:]        
    elif i == 'ц':
        a = a[:k]+a[k].replace('ц','ъ')+a[k+1:]    
    elif i == 'ч':
        a = a[:k]+a[k].replace('ч','ы')+a[k+1:]     
    elif i == 'ш':
        a = a[:k]+a[k].replace('ш','ь')+a[k+1:]     
    elif i == 'щ':
        a = a[:k]+a[k].replace('щ','э')+a[k+1:]   
    elif i == 'Ъ':
        a = a[:k]+a[k].replace('ъ','ю')+a[k+1:]
    elif i == 'ы':
        a = a[:k]+a[k].replace('ы','я')+a[k+1:]   
    elif i == 'ь':
        a = a[:k]+a[k].replace('ь','а')+a[k+1:]      
    elif i == 'э':
        a = a[:k]+a[k].replace('э','б')+a[k+1:]     
    elif i == 'ю':
        a = a[:k]+a[k].replace('ю','в')+a[k+1:]
    elif i == 'я':
        a = a[:k]+a[k].replace('я','г')+a[k+1:]
    return a