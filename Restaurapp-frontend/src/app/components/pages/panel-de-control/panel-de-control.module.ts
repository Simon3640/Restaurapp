import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';

import { PanelDeControlRoutingModule } from './panel-de-control-routing.module';
import { PanelDeControlComponent } from './panel-de-control.component';
import { NewCategoryComponent } from './new-category/new-category.component';
import { NewProductComponent } from './new-product/new-product.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

const myComponents = [NewCategoryComponent, NewProductComponent]

@NgModule({
  declarations: [
    PanelDeControlComponent, ...myComponents
  ],
  imports: [
    CommonModule,
    PanelDeControlRoutingModule,
    RouterModule,
    FormsModule,
    ReactiveFormsModule
  ],
  exports: [...myComponents]
})
export class PanelDeControlModule { }
