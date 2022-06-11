import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { PanelDeControlRoutingModule } from './panel-de-control-routing.module';
import { PanelDeControlComponent } from './panel-de-control.component';
import { NewCategoryComponent } from './new-category/new-category.component';
import { NewProductComponent } from './new-product/new-product.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { NgSelectModule } from '@ng-select/ng-select';
import { ProductPanelComponent } from './product-panel/product-panel.component';
import { EditProductComponent } from './edit-product/edit-product.component';

const myComponents = [NewCategoryComponent, NewProductComponent, ProductPanelComponent, EditProductComponent]

@NgModule({
  declarations: [
    PanelDeControlComponent, ...myComponents
  ],
  imports: [
    CommonModule,
    PanelDeControlRoutingModule,
    RouterModule,
    FormsModule,
    NgSelectModule,
    ReactiveFormsModule,
  ],
  exports: [...myComponents]
})
export class PanelDeControlModule { }
