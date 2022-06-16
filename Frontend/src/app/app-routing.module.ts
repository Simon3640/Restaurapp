import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  { path: '',
   redirectTo: 'home',
    pathMatch: 'full' 
  },
  
  { path: 'home',
   loadChildren: () => 
   import('./components/pages/home/home.module').then(m => m.HomeModule)
  }, 
  
  { path: 'products-list/:id', loadChildren: () => 
  import('./components/pages/products/products-list/products-list.module').then(m => m.ProductsListModule) 
  }, 
  
  { path: 'product-details/:id', loadChildren: () => 
  import('./components/pages/products/product-details/product-details.module').then(m => m.ProductDetailsModule) 
  },
  
  { path: 'category', loadChildren: () =>
   import('./components/pages/products/category/category.module').then(m => m.CategoryModule) 
  },
 
   { path: 'panel-de-control', loadChildren: () =>
   import('./components/pages/panel-de-control/panel-de-control.module').then(m => m.PanelDeControlModule) 
  },
  
   { path: 'new_category', loadChildren: () =>
   import('./components/pages/panel-de-control/new-category/new-category.module').then(m => m.NewCategoryModule) 
  },
  
   { path: 'new_product', loadChildren: () =>
   import('./components/pages/panel-de-control/new-product/new-product.module').then(m => m.NewProductModule) 
  },
  
   { path: 'product-panel', loadChildren: () =>
   import('./components/pages/panel-de-control/product-panel/product-panel.module').then(m => m.ProductPanelModule) 
  },
  
   { path: 'edit-product/:id', loadChildren: () =>
   import('./components/pages/panel-de-control/edit-product/edit-product.module').then(m => m.EditProductModule) 
  },
  { path: 'order-control', loadChildren: () => import('./components/pages/panel-de-control/order-control/order-control.module').then(m => m.OrderControlModule) },
]
@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
