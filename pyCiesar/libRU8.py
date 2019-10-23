def lb(i,k,a):
    if i == 'а':
        a = a[:k]+a[k].replace('а','з')+a[k+1:]        
    elif i == 'б':
        a = a[:k]+a[k].replace('б','и')+a[k+1:]        
    elif i == 'в':
        a = a[:k]+a[k].replace('в','й')+a[k+1:]       
    elif i == 'г':
        a = a[:k]+a[k].replace('г','к')+a[k+1:]        
    elif i == 'д':
        a = a[:k]+a[k].replace('д','л')+a[k+1:]      
    elif i == 'е':
        a = a[:k]+a[k].replace('е','м')+a[k+1:]        
    elif i == 'ё':
        a = a[:k]+a[k].replace('ё','н')+a[k+1:]        
    elif i == 'ж':
        a = a[:k]+a[k].replace('ж','о')+a[k+1:]       
    elif i == 'з':
        a = a[:k]+a[k].replace('з','п')+a[k+1:]        
    elif i == 'и':
        a = a[:k]+a[k].replace('и','р')+a[k+1:]      
    elif i == 'й':
        a = a[:k]+a[k].replace('й','с')+a[k+1:]        
    elif i == 'к':
        a = a[:k]+a[k].replace('к','т')+a[k+1:]        
    elif i == 'л':
        a = a[:k]+a[k].replace('л','у')+a[k+1:]       
    elif i == 'м':
        a = a[:k]+a[k].replace('м','ф')+a[k+1:]       
    elif i == 'н':
        a = a[:k]+a[k].replace('н','х')+a[k+1:]      
    elif i == 'о':
        a = a[:k]+a[k].replace('о','ц')+a[k+1:]     
    elif i == 'п':
        a = a[:k]+a[k].replace('п','ч')+a[k+1:]        
    elif i == 'р':
        a = a[:k]+a[k].replace('р','ш')+a[k+1:]      
    elif i == 'с':
        a = a[:k]+a[k].replace('с','щ')+a[k+1:]      
    elif i == 'т':
        a = a[:k]+a[k].replace('т','ъ')+a[k+1:]     
    elif i == 'у':
        a = a[:k]+a[k].replace('у','ы')+a[k+1:]      
    elif i == 'ф':
        a = a[:k]+a[k].replace('ф','ь')+a[k+1:]       
    elif i == 'х':
        a = a[:k]+a[k].replace('х','э')+a[k+1:]        
    elif i == 'ц':
        a = a[:k]+a[k].replace('ц','ю')+a[k+1:]    
    elif i == 'ч':
        a = a[:k]+a[k].replace('ч','я')+a[k+1:]     
    elif i == 'ш':
        a = a[:k]+a[k].replace('ш','а')+a[k+1:]     
    elif i == 'щ':
        a = a[:k]+a[k].replace('щ','б')+a[k+1:]   
    elif i == 'Ъ':
        a = a[:k]+a[k].replace('ъ','в')+a[k+1:]
    elif i == 'ы':
        a = a[:k]+a[k].replace('ы','г')+a[k+1:]   
    elif i == 'ь':
        a = a[:k]+a[k].replace('ь','д')+a[k+1:]      
    elif i == 'э':
        a = a[:k]+a[k].replace('э','е')+a[k+1:]     
    elif i == 'ю':
        a = a[:k]+a[k].replace('ю','ё')+a[k+1:]
    elif i == 'я':
        a = a[:k]+a[k].replace('я','ж')+a[k+1:]
    return a