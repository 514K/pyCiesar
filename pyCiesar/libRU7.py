def lb(i,k,a):
    if i == 'а':
        a = a[:k]+a[k].replace('а','ж')+a[k+1:]        
    elif i == 'б':
        a = a[:k]+a[k].replace('б','з')+a[k+1:]        
    elif i == 'в':
        a = a[:k]+a[k].replace('в','и')+a[k+1:]       
    elif i == 'г':
        a = a[:k]+a[k].replace('г','й')+a[k+1:]        
    elif i == 'д':
        a = a[:k]+a[k].replace('д','к')+a[k+1:]      
    elif i == 'е':
        a = a[:k]+a[k].replace('е','л')+a[k+1:]        
    elif i == 'ё':
        a = a[:k]+a[k].replace('ё','м')+a[k+1:]        
    elif i == 'ж':
        a = a[:k]+a[k].replace('ж','н')+a[k+1:]       
    elif i == 'з':
        a = a[:k]+a[k].replace('з','о')+a[k+1:]        
    elif i == 'и':
        a = a[:k]+a[k].replace('и','п')+a[k+1:]      
    elif i == 'й':
        a = a[:k]+a[k].replace('й','р')+a[k+1:]        
    elif i == 'к':
        a = a[:k]+a[k].replace('к','с')+a[k+1:]        
    elif i == 'л':
        a = a[:k]+a[k].replace('л','т')+a[k+1:]       
    elif i == 'м':
        a = a[:k]+a[k].replace('м','у')+a[k+1:]       
    elif i == 'н':
        a = a[:k]+a[k].replace('н','ф')+a[k+1:]      
    elif i == 'о':
        a = a[:k]+a[k].replace('о','х')+a[k+1:]     
    elif i == 'п':
        a = a[:k]+a[k].replace('п','ц')+a[k+1:]        
    elif i == 'р':
        a = a[:k]+a[k].replace('р','ч')+a[k+1:]      
    elif i == 'с':
        a = a[:k]+a[k].replace('с','ш')+a[k+1:]      
    elif i == 'т':
        a = a[:k]+a[k].replace('т','щ')+a[k+1:]     
    elif i == 'у':
        a = a[:k]+a[k].replace('у','ъ')+a[k+1:]      
    elif i == 'ф':
        a = a[:k]+a[k].replace('ф','ы')+a[k+1:]       
    elif i == 'х':
        a = a[:k]+a[k].replace('х','ь')+a[k+1:]        
    elif i == 'ц':
        a = a[:k]+a[k].replace('ц','э')+a[k+1:]    
    elif i == 'ч':
        a = a[:k]+a[k].replace('ч','ю')+a[k+1:]     
    elif i == 'ш':
        a = a[:k]+a[k].replace('ш','я')+a[k+1:]     
    elif i == 'щ':
        a = a[:k]+a[k].replace('щ','а')+a[k+1:]   
    elif i == 'Ъ':
        a = a[:k]+a[k].replace('ъ','б')+a[k+1:]
    elif i == 'ы':
        a = a[:k]+a[k].replace('ы','в')+a[k+1:]   
    elif i == 'ь':
        a = a[:k]+a[k].replace('ь','г')+a[k+1:]      
    elif i == 'э':
        a = a[:k]+a[k].replace('э','д')+a[k+1:]     
    elif i == 'ю':
        a = a[:k]+a[k].replace('ю','е')+a[k+1:]
    elif i == 'я':
        a = a[:k]+a[k].replace('я','ё')+a[k+1:]
    return a