import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ProductPanelComponent } from './product-panel.component';

const routes: Routes = [{ path: '', component: ProductPanelComponent }];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ProductPanelRoutingModule { }
